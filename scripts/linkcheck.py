#!/usr/bin/env python3
"""
Offline link checker for the built MkDocs site.

Walks every .html file under <site_dir>, parses out <a href="..."> and
<img src="...">, and verifies that:

  - relative links resolve to a file on disk
  - anchors (#id) actually exist in the target page
  - external links (http/https) are NOT checked (offline only)

Usage:  python3 scripts/linkcheck.py site/

Exit code is non-zero if any broken link is found.
"""
from __future__ import annotations
import re, sys
from pathlib import Path
from urllib.parse import urlparse, unquote

RE_HREF = re.compile(r'\bhref="([^"]+)"')
RE_SRC  = re.compile(r'\bsrc="([^"]+)"')
RE_ID   = re.compile(r'\bid="([^"]+)"')


def main(root: str) -> int:
    base = Path(root).resolve()
    if not base.is_dir():
        print(f"site dir not found: {base}", file=sys.stderr)
        return 2

    pages = list(base.rglob("*.html"))
    print(f"Checking {len(pages)} HTML files under {base}")

    # Cache id sets per-page so anchor resolution is fast.
    ids_for: dict[Path, set[str]] = {}

    def get_ids(p: Path) -> set[str]:
        if p not in ids_for:
            try:
                ids_for[p] = set(RE_ID.findall(p.read_text(errors="replace")))
            except Exception:
                ids_for[p] = set()
        return ids_for[p]

    broken: list[str] = []
    for page in pages:
        try:
            html = page.read_text(errors="replace")
        except Exception as e:
            broken.append(f"{page}: read error {e}")
            continue
        for m in list(RE_HREF.finditer(html)) + list(RE_SRC.finditer(html)):
            url = m.group(1).strip()
            parsed = urlparse(url)
            # Skip externals & data: & mailto: & tel:
            if parsed.scheme in ("http", "https", "mailto", "tel", "data"):
                continue
            if url.startswith("#"):
                # in-page anchor
                anchor = url[1:]
                if anchor and anchor not in get_ids(page):
                    broken.append(f"{page.relative_to(base)} -> #{anchor} (missing id)")
                continue
            # Resolve relative URL
            target = (page.parent / unquote(parsed.path)).resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                broken.append(f"{page.relative_to(base)} -> {url} (target missing)")
                continue
            if parsed.fragment:
                if parsed.fragment not in get_ids(target):
                    broken.append(f"{page.relative_to(base)} -> {url} "
                                  f"(missing #{parsed.fragment})")

    if broken:
        print(f"\n{len(broken)} broken links:", file=sys.stderr)
        for b in broken:
            print("  " + b, file=sys.stderr)
        return 1
    print("All links OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "site"))
