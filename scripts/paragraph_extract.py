#!/usr/bin/env python3
"""Extract paragraphs with CJK from .en.md files, paired with Chinese source.

Produces JSON on stdout mapping file_path -> list of {block, zh_block, start_line}.

Each block is one or more consecutive lines that form a logical paragraph.
The zh_block is the corresponding Chinese paragraph from the .md source.
"""

import json, os, re, sys

CJK = re.compile(r'[一-鿿]')
DOCS_ROOT = os.path.join(os.path.dirname(__file__), '..', 'docs')


def split_frontmatter(text):
    """Split text into (frontmatter, body). Frontmatter includes --- delimiters."""
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            return parts[0] + '---' + parts[1] + '---', parts[2]
    return '', text


def is_table_line(line):
    return line.strip().startswith('|')


def is_code_fence(line):
    return line.strip().startswith('```')


def is_image_line(line):
    return line.strip().startswith('![')


def is_heading(line):
    return line.strip().startswith('#')


def should_skip_block(lines):
    """Skip pure table blocks and pure code blocks."""
    text = ''.join(lines)
    stripped = text.strip()
    if not stripped:
        return True
    if all(is_table_line(l) or not l.strip() for l in lines):
        return True
    if stripped.startswith('```') and stripped.endswith('```'):
        return True
    return False


def group_paragraphs(body_lines):
    """Split body lines into paragraph blocks.

    A block is a group of contiguous non-blank lines.
    Tables are kept as separate blocks (they can contain CJK in image alt text).
    """
    blocks = []
    current = []
    start_line = 0

    for i, line in enumerate(body_lines):
        if line.strip() == '':
            if current:
                blocks.append((start_line, current))
                current = []
            # Blank lines are their own zero-line block for alignment purposes
            blocks.append((i, []))
        else:
            if not current:
                start_line = i
            current.append(line)

    if current:
        blocks.append((start_line, current))

    return blocks


def blocks_equal(a, b):
    """Check if two lists of blocks have the same non-empty count."""
    a_nonempty = [blk for _, blk in a if blk]
    b_nonempty = [blk for _, blk in b if blk]
    return len(a_nonempty) == len(b_nonempty)


def extract_pairs(en_path):
    """Extract CJK paragraph pairs from one .en.md file."""
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

    # For alignment, walk zh_body_lines and find corresponding blocks
    # Since .en.md was generated from .md, blocks should align positionally
    zh_blocks = group_paragraphs(zh_body_lines)

    # Align blocks: walk both lists, match non-empty blocks
    pairs = []

    en_idx = 0
    zh_idx = 0

    while en_idx < len(en_blocks):
        en_start, en_lines = en_blocks[en_idx]

        # Skip blank-line markers in both
        if not en_lines:
            en_idx += 1
            if zh_idx < len(zh_blocks) and not zh_blocks[zh_idx][1]:
                zh_idx += 1
            continue

        # Find next non-empty zh block
        while zh_idx < len(zh_blocks) and not zh_blocks[zh_idx][1]:
            zh_idx += 1

        if zh_idx >= len(zh_blocks):
            break

        zh_start, zh_lines = zh_blocks[zh_idx]

        # Check if en block has CJK
        en_text_block = ''.join(en_lines)
        if CJK.search(en_text_block) and not should_skip_block(en_lines):
            # Include the body line offset (en_body starts at line 0 of body)
            body_line_offset = en_fm.count('\n') if en_fm else 0
            pairs.append({
                'start_line': body_line_offset + en_start,
                'num_lines': len(en_lines),
                'en_lines': en_lines,
                'zh_lines': zh_lines,
            })

        en_idx += 1
        zh_idx += 1

    return pairs


def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(DOCS_ROOT, 'multimedia', 'mpp')

    all_pairs = {}
    total_blocks = 0
    total_cjk = 0

    for name in sorted(os.listdir(target_dir)):
        if not name.endswith('.en.md'):
            continue
        en_path = os.path.join(target_dir, name)
        pairs = extract_pairs(en_path)

        if pairs:
            rel_path = os.path.relpath(en_path, DOCS_ROOT)
            all_pairs[rel_path] = pairs
            for p in pairs:
                total_cjk += len(CJK.findall(''.join(p['en_lines'])))
            total_blocks += len(pairs)

    print(json.dumps(all_pairs, ensure_ascii=False, indent=2), file=sys.stderr)
    print(f'Extracted {total_blocks} blocks with {total_cjk} CJK chars from {len(all_pairs)} files', file=sys.stderr)

    # Output to stdout
    json.dump(all_pairs, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
