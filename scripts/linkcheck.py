#!/usr/bin/env python3
"""
Offline link checker for the built MkDocs site.

Walks every .html file under <site_dir>, parses out <a href="..."> and
<img src="...">, and verifies that:

  - relative + site-absolute links resolve to a file on disk
  - anchors (#id) actually exist in the target page
  - external links (http/https) are NOT checked (offline only)

Honors the `site_url` from mkdocs.yml — links that point to the deploy
prefix (e.g. /hi3403-docs/foo) are resolved against the site root, not
the page directory.

Categorises issues so a long report stays readable:
  - missing-page    : link points to a file that doesn't exist
  - missing-anchor  : page exists but the #id is missing
  - junk            : javascript:void(0), mailto:, etc. (skipped)

Usage:
    python3 scripts/linkcheck.py site/
    python3 scripts/linkcheck.py site/ --section get-started
        (only check pages under that path)
    python3 scripts/linkcheck.py site/ --no-anchors
        (skip the anchor-target check; useful when migrated docs have
         many cross-doc anchor references)

Exit code is non-zero if any broken link is found.
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path
from urllib.parse import urlparse, unquote

RE_HREF = re.compile(r'\bhref="([^"]+)"')
RE_SRC  = re.compile(r'\bsrc="([^"]+)"')
RE_ID   = re.compile(r'\bid="([^"]+)"')
RE_NAME = re.compile(r'\ba\s+name="([^"]+)"')   # legacy <a name="x"> anchors


def find_site_root(start: Path) -> Path:
    """
    Detect the deploy prefix. MkDocs writes the prefix into the rendered
    HTML (e.g. <link rel="canonical" href="https://.../hi3403-docs/...">).
    We look at the index page and match the first canonical/og:url link.
    """
    idx = start / "index.html"
    if not idx.is_file():
        return start
    html = idx.read_text(errors="replace")
    m = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
    if not m:
        m = re.search(r'<meta\s+property="og:url"\s+content="([^"]+)"', html)
    if not m:
        return start
    parsed = urlparse(m.group(1))
    return parsed.path.rstrip("/")  # str path like "/hi3403-docs"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("site", nargs="?", default="site")
    ap.add_argument("--section", default=None,
                    help="Only check pages under this top-level section")
    ap.add_argument("--no-anchors", action="store_true",
                    help="Skip per-anchor checks (target page existence still verified)")
    ap.add_argument("--summary-only", action="store_true",
                    help="Print only counts, not every broken link")
    args = ap.parse_args(argv)

    base = Path(args.site).resolve()
    if not base.is_dir():
        print(f"site dir not found: {base}", file=sys.stderr)
        return 2

    deploy_prefix = find_site_root(base)
    if isinstance(deploy_prefix, str) and deploy_prefix:
        # Site is served at /<prefix>/... — when we see an absolute URL
        # starting with /<prefix>/foo, we resolve to <base>/foo.
        prefix = deploy_prefix.lstrip("/")
        print(f"detected deploy prefix: /{prefix}/")
    else:
        prefix = ""
        print("no deploy prefix detected — using site root")

    pages = list(base.rglob("*.html"))
    if args.section:
        pages = [p for p in pages if args.section in str(p.relative_to(base))]
    print(f"Checking {len(pages)} HTML files\n")

    # Cache id+name sets per-page so anchor resolution is fast.
    ids_for: dict[Path, set[str]] = {}

    def get_ids(p: Path) -> set[str]:
        if p not in ids_for:
            try:
                txt = p.read_text(errors="replace")
                ids_for[p] = set(RE_ID.findall(txt)) | set(RE_NAME.findall(txt))
            except Exception:
                ids_for[p] = set()
        return ids_for[p]

    missing_pages: list[str] = []
    missing_anchors: list[str] = []

    for page in pages:
        try:
            html = page.read_text(errors="replace")
        except Exception as e:
            missing_pages.append(f"{page.relative_to(base)}: read error {e}")
            continue
        for m in list(RE_HREF.finditer(html)) + list(RE_SRC.finditer(html)):
            url = m.group(1).strip()
            parsed = urlparse(url)

            # Skip externals & junk schemes.
            if parsed.scheme in ("http", "https", "mailto", "tel", "data"):
                continue
            if url.startswith("javascript:"):
                continue

            if url.startswith("#"):
                # in-page anchor
                anchor = url[1:]
                if anchor and not args.no_anchors and anchor not in get_ids(page):
                    missing_anchors.append(
                        f"{page.relative_to(base)} -> #{anchor}")
                continue

            # Resolve URL to disk path.
            url_path = unquote(parsed.path)
            if url_path.startswith("/"):
                # Absolute. Strip the deploy prefix if present.
                if prefix and url_path.startswith(f"/{prefix}/"):
                    url_path = url_path[len(prefix) + 1:]  # leave leading /
                target = (base / url_path.lstrip("/")).resolve()
            else:
                target = (page.parent / url_path).resolve()

            if target.is_dir():
                target = target / "index.html"

            # If link is a directory served as <foo>/, MkDocs writes it
            # without the .html — check both.
            if not target.exists() and not target.suffix:
                target = target.with_suffix(".html")

            if not target.exists():
                missing_pages.append(f"{page.relative_to(base)} -> {url}")
                continue

            if parsed.fragment and not args.no_anchors:
                if parsed.fragment not in get_ids(target):
                    missing_anchors.append(
                        f"{page.relative_to(base)} -> {url}")

    # ---- Report ------------------------------------------------------
    print(f"  missing pages:   {len(missing_pages)}")
    print(f"  missing anchors: {len(missing_anchors)}")
    print()

    if not args.summary_only:
        if missing_pages:
            print(f"=== Missing pages ({len(missing_pages)}) ===")
            seen = set()
            for b in missing_pages:
                if b in seen: continue
                seen.add(b)
                print("  " + b)
            print()
        if missing_anchors and not args.no_anchors:
            print(f"=== Missing anchors ({len(missing_anchors)}) ===")
            # Anchor reports are noisy; show top 30 unique.
            seen = set()
            for b in missing_anchors:
                if b in seen: continue
                seen.add(b)
                if len(seen) > 30:
                    print(f"  ... ({len(set(missing_anchors)) - 30} more)")
                    break
                print("  " + b)

    if missing_pages or (missing_anchors and not args.no_anchors):
        return 1
    print("All links OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
