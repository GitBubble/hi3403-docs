#!/usr/bin/env python3
"""
Rewrite Markdown-only image URLs (![](figures/...) in docs/**/*.en.md)
to match sibling Chinese *.md paths, preserving English alt text and titles.

Alignment uses SequenceMatcher over figure basenames, with greedy fuzzy pairing
for any entries that pairwise alignment leaves unmatched.
"""

from __future__ import annotations

import re
from difflib import SequenceMatcher
from pathlib import PurePosixPath, Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

IMG_MD = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<body>[^)]+)\)")


def parse_paren(inner: str) -> tuple[str, str | None]:
    inner = inner.strip()
    m = re.fullmatch(r'(\S+)(?:\s+"([^"]*)")?', inner)
    if not m:
        return inner, None
    return m.group(1), m.group(2)


def norm_fig(url: str) -> str | None:
    u = PurePosixPath(url.split("#", 1)[0]).as_posix()
    while u.startswith("./"):
        u = u[2:]
    return u if u.startswith("figures/") else None


def basename_ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def collect_fig_chunks(text: str) -> list[tuple[int, int, str, str, str | None]]:
    chunks: list[tuple[int, int, str, str, str | None]] = []
    for m in IMG_MD.finditer(text):
        raw_url, tt = parse_paren(m.group("body"))
        nf = norm_fig(raw_url)
        if nf is None:
            continue
        chunks.append((m.start(), m.end(), m.group("alt"), nf, tt))
    return chunks


def align_ix(eb: list[str], zb: list[str]) -> dict[int, int]:
    mp: dict[int, int] = {}
    sm = SequenceMatcher(None, eb, zb, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                mp[i1 + k] = j1 + k
        elif tag == "replace":
            rn, rz = i2 - i1, j2 - j1
            L = min(rn, rz)
            for k in range(L):
                mp[i1 + k] = j1 + k

    used = set(mp.values())

    needy_en = [i for i in range(len(eb)) if i not in mp]
    zh_unused = [j for j in range(len(zb)) if j not in used]

    while needy_en and zh_unused:
        ei = needy_en.pop(0)
        en_bn = eb[ei]
        best_bi = None
        best_r = -1.0
        for bi, zj in enumerate(zh_unused):
            r = basename_ratio(en_bn, zb[zj])
            if r > best_r:
                best_r = r
                best_bi = bi
        assign_j = zh_unused.pop(best_bi) if best_bi is not None else zh_unused.pop(0)
        mp[ei] = assign_j

    return mp


def apply_sync(en_txt: str, zh_txt: str) -> str | None:
    en_chunks = collect_fig_chunks(en_txt)
    zh_chunks = collect_fig_chunks(zh_txt)
    if not en_chunks:
        return None
    eb = [PurePosixPath(c[3]).name for c in en_chunks]
    zb = [PurePosixPath(c[3]).name for c in zh_chunks]
    if not zb:
        return None

    ix = align_ix(eb, zb)

    s = en_txt
    for idx in reversed(range(len(en_chunks))):
        if idx not in ix:
            continue
        st, fin, alt, _, title = en_chunks[idx]
        zi = ix[idx]
        new_url = zh_chunks[zi][3]
        if title:
            blob = f'![{alt}]({new_url} "{title}")'
        else:
            blob = f"![{alt}]({new_url})"
        s = s[:st] + blob + s[fin:]

    return s


def main() -> int:
    changed: list[str] = []

    for en_path in sorted(DOCS.rglob("*.en.md")):
        zh_path = en_path.with_name(en_path.name.replace(".en.md", ".md"))
        if not zh_path.is_file():
            continue
        et = en_path.read_text(encoding="utf-8")
        zt = zh_path.read_text(encoding="utf-8")
        new_t = apply_sync(et, zt)
        if new_t is None or new_t == et:
            continue
        en_path.write_text(new_t, encoding="utf-8", newline="\n")
        changed.append(str(en_path.relative_to(DOCS)))

    print(f"sync_en_figure_paths: rewrote Markdown figure paths in {len(changed)} files")
    for line in sorted(changed)[:50]:
        print(f"  + {line}")
    if len(changed) > 50:
        print(f"  ... {len(changed) - 50} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
