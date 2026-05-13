#!/usr/bin/env python3
"""Paragraph-level Chinese→English re-translation for MPP docs.

Usage:
    python scripts/retranslate.py extract [FILE ...]  → writes translations_needed.json
    python scripts/retranslate.py apply <json_file>    → patches .en.md files from translations

The extract mode finds paragraphs in .en.md that contain CJK or concatenated
English, pairs them with the Chinese source paragraph from the .md file, and
outputs a JSON file ready for translation.
"""

import hashlib, json, os, re, sys

CJK = re.compile(r'[一-鿿]')
CONCAT = re.compile(r'[a-z][A-Z]')
DOCS_ROOT = os.path.join(os.path.dirname(__file__), '..', 'docs')


# ═══════════════════════════════════════════════════════════════════════
# Utilities
# ═══════════════════════════════════════════════════════════════════════

def split_frontmatter(text):
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            return parts[0] + '---' + parts[1] + '---', parts[2]
    return '', text


def block_hash(lines):
    """Stable hash of a list of lines for matching."""
    return hashlib.md5('\n'.join(lines).encode()).hexdigest()[:12]


# ═══════════════════════════════════════════════════════════════════════
# Paragraph grouping
# ═══════════════════════════════════════════════════════════════════════

def group_paragraphs(lines):
    """Split lines into paragraph blocks with start-line and line list."""
    blocks = []
    current = []
    start = 0
    for i, line in enumerate(lines):
        if line.strip() == '':
            if current:
                blocks.append((start, current))
                current = []
            blocks.append((i, []))
        else:
            if not current:
                start = i
            current.append(line)
    if current:
        blocks.append((start, current))
    return blocks


def is_table_block(lines):
    return all(l.strip().startswith('|') or l.strip() == '' for l in lines)


def is_image_block(lines):
    return any(l.strip().startswith('![') for l in lines)


def is_code_block(lines):
    text = '\n'.join(lines).strip()
    return text.startswith('```') and text.endswith('```')


# ═══════════════════════════════════════════════════════════════════════
# Anchor-based alignment
# ═══════════════════════════════════════════════════════════════════════

def find_anchors(lines):
    """Return set of line indices that are structural anchors (headings, tables, fences)."""
    anchors = set()
    in_fence = False
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith('```'):
            in_fence = not in_fence
            anchors.add(i)
        elif not in_fence:
            if s.startswith('#'):
                anchors.add(i)
            elif s.startswith('|') and '|' in s[1:]:
                anchors.add(i)
            elif s.startswith('!['):
                anchors.add(i)
            elif s.startswith('<a name='):
                anchors.add(i)
    return anchors


def align_zh_to_en(en_body_lines, zh_body_lines, en_block_start, en_block_end):
    """Find the zh block corresponding to en_block[start:end].

    Uses proximity to nearest anchors to verify alignment.
    Returns (zh_start, zh_end) or None if alignment fails.
    """
    en_anchors = find_anchors(en_body_lines)
    zh_anchors = find_anchors(zh_body_lines)

    # Find nearest anchor above en_block_start
    anchor_above = None
    for i in range(en_block_start, -1, -1):
        if i in en_anchors:
            anchor_above = i
            break

    # Find matching anchor in zh
    if anchor_above is not None:
        anchor_line = en_body_lines[anchor_above]
        # Search in zh around the same position
        search_start = max(0, anchor_above - 50)
        search_end = min(len(zh_body_lines), anchor_above + 50)
        for i in range(search_start, search_end):
            if i in zh_anchors and zh_body_lines[i].strip() == anchor_line.strip():
                # Found matching anchor; offset from anchor
                zh_offset = en_block_start - anchor_above
                zh_block_start = i + zh_offset
                zh_block_end = zh_block_start + (en_block_end - en_block_start)
                if zh_block_start >= 0 and zh_block_end <= len(zh_body_lines):
                    return zh_block_start, zh_block_end
                break

    # Fallback: simple positional alignment
    ratio = len(zh_body_lines) / max(1, len(en_body_lines))
    zh_start = int(en_block_start * ratio)
    zh_end = int(en_block_end * ratio)
    return zh_start, min(zh_end, len(zh_body_lines))


# ═══════════════════════════════════════════════════════════════════════
# Main extraction
# ═══════════════════════════════════════════════════════════════════════

def extract_blocks(en_path):
    """Extract blocks needing re-translation from one .en.md file."""
    zh_path = en_path.replace('.en.md', '.md')
    if not os.path.exists(zh_path):
        return []

    with open(en_path, 'r', encoding='utf-8') as f:
        en_text = f.read()
    with open(zh_path, 'r', encoding='utf-8') as f:
        zh_text = f.read()

    en_fm, en_body = split_frontmatter(en_text)
    zh_fm, zh_body = split_frontmatter(zh_text)

    en_body_lines = en_body.split('\n')
    zh_body_lines = zh_body.split('\n')

    en_blocks = group_paragraphs(en_body_lines)
    zh_blocks = group_paragraphs(zh_body_lines)

    body_offset = en_fm.count('\n') if en_fm else 0
    results = []

    en_idx = zh_idx = 0
    while en_idx < len(en_blocks):
        en_start, en_lines = en_blocks[en_idx]

        # Skip empty markers
        if not en_lines:
            en_idx += 1
            if zh_idx < len(zh_blocks) and not zh_blocks[zh_idx][1]:
                zh_idx += 1
            continue

        # Skip non-text blocks
        if is_table_block(en_lines) or is_image_block(en_lines) or is_code_block(en_lines):
            en_idx += 1
            if zh_idx < len(zh_blocks):
                zh_idx += 1
            continue

        # Find next non-empty zh block
        while zh_idx < len(zh_blocks) and not zh_blocks[zh_idx][1]:
            zh_idx += 1
        if zh_idx >= len(zh_blocks):
            break

        zh_start, zh_lines = zh_blocks[zh_idx]

        en_text_block = '\n'.join(en_lines)
        zh_text_block = '\n'.join(zh_lines)

        cjk_count = len(CJK.findall(en_text_block))
        has_concat = bool(CONCAT.search(en_text_block))

        # Include blocks with CJK OR concatenation (even 0 CJK can be garbled)
        if (cjk_count > 0 or has_concat) and en_lines:
            results.append({
                'line': body_offset + en_start,
                'num': len(en_lines),
                'hash': block_hash(en_lines),
                'cjk': cjk_count,
                'concat': has_concat,
                'en': en_lines,
                'zh': zh_lines,
            })

        en_idx += 1
        zh_idx += 1

    return results


# ═══════════════════════════════════════════════════════════════════════
# Application
# ═══════════════════════════════════════════════════════════════════════

def apply_translations(translations_json_path):
    """Read translations JSON and patch .en.md files."""
    with open(translations_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    stats = {'files': 0, 'blocks': 0, 'applied': 0, 'skipped': 0}

    for rel_path, blocks in data.items():
        en_path = os.path.join(DOCS_ROOT, rel_path)
        if not os.path.exists(en_path):
            print(f'WARNING: {en_path} not found, skipping', file=sys.stderr)
            stats['skipped'] += len(blocks)
            continue

        with open(en_path, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.split('\n')
        stats['files'] += 1

        # Sort blocks by line number descending so replacements don't shift positions
        sorted_blocks = sorted(blocks, key=lambda b: b['line'], reverse=True)

        for block in sorted_blocks:
            if 'translation' not in block or not block['translation']:
                stats['skipped'] += 1
                continue

            start = block['line']
            end = start + block['num']
            translation = block['translation']

            # Verify content hash matches
            original = '\n'.join(lines[start:end])
            if block_hash(lines[start:end]) != block.get('hash', ''):
                print(f'WARNING: hash mismatch at {rel_path}:{start}, '
                      f'skipping (file may have changed)', file=sys.stderr)
                stats['skipped'] += 1
                continue

            # Replace: remove old lines, insert new lines
            new_lines = translation.split('\n')
            lines[start:end] = new_lines
            stats['applied'] += 1
            stats['blocks'] += 1

        # Write back
        with open(en_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        print(f'Patched {rel_path}: {stats["applied"]} blocks', file=sys.stderr)

    print(f'\nTotal: {stats["files"]} files, {stats["applied"]} blocks applied, '
          f'{stats["skipped"]} skipped', file=sys.stderr)


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def cmd_extract(args):
    out_file = None
    targets = []

    for a in args:
        if a.endswith('.json'):
            out_file = a
        else:
            targets.append(a)

    if not targets:
        mpp_dir = os.path.join(DOCS_ROOT, 'multimedia', 'mpp')
        for name in sorted(os.listdir(mpp_dir)):
            if name.endswith('.en.md'):
                targets.append(os.path.join(mpp_dir, name))

    all_data = {}
    total_blocks = 0
    total_cjk = 0

    for path in targets:
        blocks = extract_blocks(path)
        if blocks:
            rel = os.path.relpath(path, DOCS_ROOT)
            all_data[rel] = blocks
            total_blocks += len(blocks)
            total_cjk += sum(b['cjk'] for b in blocks)

    if out_file:
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        print(f'Wrote {out_file}', file=sys.stderr)
    else:
        json.dump(all_data, sys.stdout, ensure_ascii=False, indent=2)

    concat_blocks = sum(1 for blocks in all_data.values() for b in blocks if b['concat'])
    print(f'Extracted {total_blocks} blocks ({total_cjk} CJK chars, '
          f'{concat_blocks} with concatenation) from {len(all_data)} files', file=sys.stderr)


def cmd_apply(args):
    if not args:
        print('Usage: retranslate.py apply <translations.json>', file=sys.stderr)
        sys.exit(1)
    apply_translations(args[0])


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1]
    rest = sys.argv[2:]

    if cmd == 'extract':
        cmd_extract(rest)
    elif cmd == 'apply':
        cmd_apply(rest)
    else:
        print(f'Unknown command: {cmd}', file=sys.stderr)
        print(__doc__, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
