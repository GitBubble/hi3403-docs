#!/usr/bin/env python3
"""Multi-pass CJK→English translator for MPP documentation.

Usage:
    python scripts/translate.py [--passes N] [--deconcat] [--dry-run] [FILE ...]
    python scripts/translate.py --extract-notes [FILE ...]

    If no FILE is given, translates all *.en.md files under docs/ that still
    contain Chinese text.

Passes (defined in phrases.py):
    1  Multi-word fixed expressions
    2  Verbs, nouns, connectives, quantifiers
    3  Single-character remnants
    4  Grammatical particle removal
    5  Strip remaining CJK + deconcatenate (requires --deconcat)
"""
import argparse, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phrases import ALL_PASSES

CJK = re.compile(r'[一-鿿㐀-䶿]')
DOCS_ROOT = os.path.join(os.path.dirname(__file__), '..', 'docs')


def count_cjk(text: str) -> int:
    return len(CJK.findall(text))


def translate_text(text: str, passes: list[list[tuple[str, str]]]) -> str:
    for phrase_list in passes:
        for zh, en in phrase_list:
            text = text.replace(zh, en)
    return text


def strip_remaining_cjk(text: str) -> str:
    """Remove any remaining CJK characters from text."""
    return CJK.sub('', text)


def translate_file(path: str, passes: list[list[tuple[str, str]]],
                   use_deconcat: bool = False) -> tuple[int, int]:
    with open(path, encoding='utf-8') as fh:
        content = fh.read()

    before = count_cjk(content)
    if before == 0:
        return 0, 0

    parts = content.split('---', 2)
    if len(parts) > 2 and parts[0].strip() == '':
        pre = parts[0] + '---' + parts[1] + '---'
        body = parts[2]
    else:
        pre = ''
        body = content

    lines = body.split('\n')
    translated = []
    for l in lines:
        if CJK.search(l):
            l = translate_text(l, passes)
        translated.append(l)

    # Pass 5: strip remaining CJK from all lines
    translated = [strip_remaining_cjk(l) for l in translated]

    # Deconcatenate
    if use_deconcat:
        from deconcat import deconcat_text
        translated = [deconcat_text(l) for l in translated]

    result = pre + '\n'.join(translated)

    after = count_cjk(result)
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(result)

    return before, after


def find_files() -> list[str]:
    paths = []
    for root, _dirs, files in os.walk(DOCS_ROOT):
        for name in files:
            if name.endswith('.en.md'):
                path = os.path.join(root, name)
                if count_cjk(open(path).read()) > 0:
                    paths.append(path)
    return sorted(paths)


def extract_notes(en_files: list[str]) -> None:
    """Extract Note sections with CJK alongside their Chinese source."""
    for en_path in en_files:
        zh_path = en_path.replace('.en.md', '.md')
        if not os.path.exists(zh_path):
            continue

        with open(en_path) as f:
            en_content = f.read()
        with open(zh_path) as f:
            zh_content = f.read()

        en_parts = en_content.split('---', 2)
        en_body = en_parts[2] if len(en_parts) > 2 else en_content
        zh_parts = zh_content.split('---', 2)
        zh_body = zh_parts[2] if len(zh_parts) > 2 else zh_content

        zh_sections = {}
        zh_blocks = zh_body.split('【注意】')
        for i in range(1, len(zh_blocks)):
            end = re.search(r'\n【|^\#', zh_blocks[i], re.MULTILINE)
            text = zh_blocks[i][:end.start()] if end else zh_blocks[i][:800]
            before = zh_body[:zh_body.find('【注意】' + text[:60])] if '【注意】' + text[:60] in zh_body else ''
            heading_match = re.findall(r'^#{1,4}\s+.+', before, re.MULTILINE)
            heading = heading_match[-1] if heading_match else 'unknown'
            zh_sections[heading.strip()] = text.strip()

        en_sections = list(re.finditer(r'\*\*Note\*\*', en_body))
        note_count = 0
        cjk_total = 0

        for m in en_sections:
            start = m.end()
            end_match = re.search(
                r'\n\*\*Example\*\*|\n\*\*Requirements\*\*|\n\*\*Return Value\*\*|'
                r'\n\*\*Syntax\*\*|\n\*\*Parameters\*\*|\n\*\*Reference\*\*|\n\#',
                en_body[start:], re.MULTILINE)
            end = start + end_match.start() if end_match else start + 800
            en_text = en_body[start:end]
            cn = count_cjk(en_text)
            if cn == 0:
                continue

            note_count += 1
            cjk_total += cn
            lineno = en_body[:m.start()].count('\n') + 1

            before = en_body[:m.start()]
            heading_match = re.findall(r'^#{1,4}\s+.+', before, re.MULTILINE)
            heading = heading_match[-1] if heading_match else 'unknown'

            zh_text = zh_sections.get(heading.strip(), '(no zh match found)')

            rel = os.path.relpath(en_path, DOCS_ROOT)
            print(f'\n{"═" * 70}')
            print(f'  {rel}:{lineno}  ({cn} CJK)  ← {heading[:60]}')
            print(f'{"═" * 70}')
            print(f'  [ZH SOURCE]')
            print(f'  {zh_text[:600]}')
            print(f'  [EN CURRENT]')
            print(f'  {en_text.strip()[:600]}')

        if note_count:
            print(f'\n  ── {note_count} sections, {cjk_total} CJK in {os.path.basename(en_path)}')


def main():
    parser = argparse.ArgumentParser(description='Multi-pass CJK→English translator')
    parser.add_argument('files', nargs='*',
                        help='Files to translate (default: all .en.md with CJK)')
    parser.add_argument('--passes', type=int, default=0, choices=[1, 2, 3, 4],
                        help='Only run this many CJK passes (default: all 4)')
    parser.add_argument('--deconcat', action='store_true',
                        help='Run deconcatenation pass after CJK removal')
    parser.add_argument('--dry-run', action='store_true',
                        help='Report CJK counts without modifying files')
    parser.add_argument('--extract-notes', action='store_true',
                        help='Extract Note sections with CJK alongside zh source for review')
    args = parser.parse_args()

    targets = args.files if args.files else find_files()

    if not targets:
        print('No files to translate.')
        return

    if args.extract_notes:
        extract_notes(targets)
        return

    passes = ALL_PASSES[:args.passes] if args.passes else ALL_PASSES

    total_before = total_after = 0
    for path in targets:
        if args.dry_run:
            with open(path, encoding='utf-8') as fh:
                cn = count_cjk(fh.read())
            print(f'{cn:>6}  {os.path.relpath(path, DOCS_ROOT)}')
            continue

        before, after = translate_file(path, passes, use_deconcat=args.deconcat)
        total_before += before
        total_after += after
        delta = before - after
        pct = (delta / before * 100) if before else 0
        print(f'{before:>6} → {after:>5}  (-{delta:>4}, {pct:3.0f}%)  '
              f'{os.path.relpath(path, DOCS_ROOT)}')

    if total_before and not args.dry_run:
        total_delta = total_before - total_after
        total_pct = (total_delta / total_before * 100) if total_before else 0
        print(f'{"─" * 60}')
        print(f'{total_before:>6} → {total_after:>5}  (-{total_delta:>4}, {total_pct:3.0f}%)  TOTAL')


if __name__ == '__main__':
    main()
