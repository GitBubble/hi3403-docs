#!/usr/bin/env python3
"""
Migrate upstream pegasus + hi3403-build docs into pegasus-docs/docs/.

Pipeline (one-shot, idempotent):

  1. Inventory: walk pegasus/docs/zh-CN/, pegasus/vendor/*/, pegasus/os/*/
     and (optionally) hi3403-build/ for .md files.
  2. Resolve destination: every source path → a slug-friendly path under
     docs/<section>/... using SLUG_MAP below (deterministic — no pinyin
     library required).
  3. Transform each doc:
        - strip generated HTML anchors `<a name="ZH-CN_TOPIC_..."></a>`
        - drop empty <a name="..."></a> companions
        - normalize line endings
        - inject YAML front-matter (title from first H1, source path)
        - rewrite internal links per the rename map
  4. Copy images / figures / public_sys-resources alongside their parent.
  5. Write inventory.csv so the user can audit the mapping.

Usage:
    python3 scripts/migrate.py \\
        --pegasus       ../pegasus \\
        --hi3403-build  ../hi3403-build \\
        --out           docs/

Flags:
    --dry-run    print what would happen, change nothing
    --force      overwrite previously-migrated files
    --no-images  skip image copies (faster iteration)
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# --------------------------------------------------------------------------
# Slug mapping
# --------------------------------------------------------------------------
# Each key is the basename of a directory inside pegasus/docs/zh-CN/.
# Each value is its destination path under docs/, relative to --out.
# Order doesn't matter; the longest-prefix-doesn't-apply because we
# look up by exact basename.
#
# When a single upstream dir maps to multiple destination files (rare),
# add a tuple of (relative_dest_dir, file_renames). For most entries we
# just point at a destination directory and the migrator copies the .md
# inside.
#
# Edit this table to reorganize the IA — it's the single source of
# truth for the migration.
SLUG_MAP: Dict[str, str] = {
    # ---- Get started ------------------------------------------------------
    "Hi3403V100环境搭建指南":               "get-started/environment",
    "驱动和开发环境安装指南":               "get-started/driver-install",
    "SS928V100╱SS927V100 SDK 安装以及升级使用说明":
                                            "get-started/sdk-install",
    # Upstream "quickstart" lands at /upstream-quickstart so the friendly
    # hand-written get-started/quickstart.md owns the canonical URL.
    "快速上手指南":                          "get-started/upstream-quickstart",

    # ---- SoC & Linux ------------------------------------------------------
    "SS928V100 超高清智能网络录像机 SoC 产品简介":
                                            "soc-linux/soc-overview",
    "SS928V100╱SS927V100 U-boot 移植应用开发指南":
                                            "soc-linux/uboot",
    "SS928V100╱SS927V100 安全启动使用指南": "soc-linux/secure-boot",
    "外围设备驱动操作指南":                 "soc-linux/peripherals",
    "内存布局调整指南":                     "soc-linux/memory-layout",
    "MIPI 使用指南":                        "soc-linux/mipi",
    "DDR 小型化指南":                       "soc-linux/ddr-tuning",
    "PCIE级联应用指南":                     "soc-linux/pcie",
    "安全子系统使用说明":                   "soc-linux/security",
    "应用开发指南":                         "soc-linux/app-dev",

    # ---- Multimedia & AI --------------------------------------------------
    "MPP 媒体处理软件 V5.0 开发参考":       "multimedia/mpp",          # multi-file
    "ISP 开发参考":                         "multimedia/isp/dev-ref",  # multi-file
    "ISP 图像调优指南":                     "multimedia/isp/tuning",
    "ISP 颜色调优说明":                     "multimedia/isp/color",
    "Sensor调试指南":                       "multimedia/isp/sensor",
    "图像分析引擎2与图像分析引擎1使用差异说明":
                                            "multimedia/isp/iae-migration",
    "图像质量调试工具使用指南":             "tools/iqs-debug",   # tool, not multimedia
    "HDMI 开发参考":                        "multimedia/hdmi",
    "图形开发用户指南":                     "multimedia/graphics/dev",
    "GFBG 开发指南":                        "multimedia/graphics/gfbg",
    "SS928V100╱SS927V100 3DNR参数配置说明": "multimedia/3dnr",
    "HNR 开发参考":                         "multimedia/cv/hnr",
    "HNR 调优指南":                         "multimedia/cv/hnr-tuning",
    "DIS 调试指南":                         "multimedia/dis",
    "DPU2.0 工具使用指南":                  "multimedia/cv/dpu",
    "MotionFusion 开发参考":                "multimedia/motionfusion",
    "黑白彩色双路融合调试指南":             "multimedia/dual-fusion/tuning",
    "黑白彩色双路融合 开发参考":            "multimedia/dual-fusion/dev",
    "抓拍使用指南":                         "multimedia/snapshot",
    "开机画面使用指南":                     "multimedia/splash",
    "SVP2.0开发指南":                       "multimedia/svp/dev",
    "ATC Graph开发指南":                    "multimedia/atc/graph",
    "ATC工具使用指南":                      "multimedia/atc/tool",
    "ATC自定义算子开发指南":                "multimedia/atc/custom-op",
    "AMCT使用指南（Caffe）":                "multimedia/amct/caffe",
    "AMCT使用指南（PyTorch）":              "multimedia/amct/pytorch",

    # ---- Tools ------------------------------------------------------------
    "BurnTool 工具使用指南":                "tools/burntool",
    "MindCmd 使用指南":                     "tools/mindcmd",
    "ToolPlatform工具平台使用指南":         "tools/toolplatform",
    "Profiling工具使用指南":                "tools/profiling",
    "精度比对工具使用指南":                 "tools/accuracy-compare",

    # ---- Reference: SYS_CONFIG, FAQs, API --------------------------------
    "SYS_CONFIG配置指南":                   "reference/sys-config",
    "BSP FAQ":                              "reference/faq/bsp",
    "ISP FAQ":                              "reference/faq/isp",
    "MPP 媒体处理软件 V5.0 FAQ":            "reference/faq/mpp",
    "拼接 FAQ":                             "reference/faq/splice",
    "CIPHER API 参考":                      "reference/api/cipher",
    "GFBG API 参考":                        "reference/api/gfbg",
    "IVE API 参考":                         "reference/api/ive",
    "IVS API参考":                          "reference/api/ivs",
    "KLAD API 参考":                        "reference/api/klad",
    "OTP API 参考":                         "reference/api/otp",
    "SVP2.0 API 参考":                      "reference/api/svp",
    "TDE API参考":                          "reference/api/tde",
    "音频组件API参考":                      "reference/api/audio",

    # ---- OS ---------------------------------------------------------------
    "OpenHarmony Small版本使用指南":        "os/openharmony/usage",
    "OpenHarmony Small系统集成Hi3403V100移植案例":
                                            "os/openharmony/porting",

    # ---- Community --------------------------------------------------------
    "release-notes":                        "community/release-notes",
}

# Per-vendor README.md mapping under pegasus/vendor/* → boards/<slug>/index.md
VENDOR_MAP: Dict[str, str] = {
    "topeet":            "boards/topeet",
    "LubanCat-Hi3403":   "boards/lubancat",
    "ebaina":            "boards/ebaina",
    "rkh":               "boards/rkh",
    "zsks":              "boards/zsks",
    # opensource/ is not a board; it's upstream tracking. Skip.
}

# OS-specific READMEs from pegasus/os/*/README*.md
OS_MAP: Dict[str, str] = {
    "Ubuntu":       "os/ubuntu",
    "OpenHarmony":  "os/openharmony",
    "OpenEuler":    "os/openeuler",
}

# --------------------------------------------------------------------------
# Anchor / boilerplate stripping regexes
# --------------------------------------------------------------------------
RE_GEN_ANCHOR = re.compile(r'<a\s+name="(?:ZH-CN_TOPIC_|p\d+|table\d+|row\d+|section\d+|figure\d+)[^"]*"></a>')
RE_EMPTY_NAME_ANCHOR = re.compile(r'<a\s+name="[^"]*"></a>')
RE_BACK_TO_TOP = re.compile(r'^\[\s*[Bb]ack\s+to\s+top\s*\].*$', re.MULTILINE)
# Some upstream docs wrap H1 with the anchor inline; clean that up:
RE_H1_WITH_ANCHOR = re.compile(r'^(#\s+.*?)<a\s+name="[^"]*"></a>\s*$', re.MULTILINE)


# --------------------------------------------------------------------------
@dataclass
class Doc:
    """One source markdown file mapped to its destination."""
    src: Path
    dest: Path                    # absolute path under --out
    rel_dest: str                 # path relative to --out (for inventory)
    title: str = ""
    images_src: List[Path] = field(default_factory=list)
    images_dest: List[Path] = field(default_factory=list)


# --------------------------------------------------------------------------
def first_h1(text: str) -> str:
    """Return the first markdown H1 (without the leading #), stripped."""
    for line in text.splitlines():
        if line.startswith("# "):
            # remove inline HTML and trailing anchors
            t = re.sub(r'<[^>]+>', '', line[2:]).strip()
            return t.strip("#").strip()
    return ""


def strip_anchors(text: str) -> str:
    """
    Clean up cosmetic noise but PRESERVE <a name="ZH-CN_TOPIC_..."></a>
    tags inside the body — internal cross-references like
    [section](#ZH-CN_TOPIC_X) target those anchors and would break if
    stripped.

    Only strip anchors from H1 lines (where they look ugly in the page
    title) and "back to top" boilerplate.
    """
    text = RE_H1_WITH_ANCHOR.sub(r"\1", text)
    text = RE_BACK_TO_TOP.sub("", text)
    return text


def inject_front_matter(text: str, title: str, source_rel: str) -> str:
    fm_lines = ["---"]
    if title:
        # YAML-quote the title to be safe with special chars
        safe = title.replace('"', '\\"')
        fm_lines.append(f'title: "{safe}"')
    fm_lines.append(f"source: {source_rel}")
    fm_lines.append("---\n\n")
    return "\n".join(fm_lines) + text


# --------------------------------------------------------------------------
def discover_docs(args) -> List[Doc]:
    pegasus = Path(args.pegasus).resolve()
    out = Path(args.out).resolve()
    docs: List[Doc] = []

    # --- pegasus/docs/zh-CN/<dir>/ ---------------------------------------
    zh = pegasus / "docs" / "zh-CN"
    if zh.is_dir():
        for sub in sorted(zh.iterdir()):
            if not sub.is_dir():
                continue
            slug = SLUG_MAP.get(sub.name)
            if slug is None:
                # Unmapped — log but skip; user can extend SLUG_MAP.
                print(f"  [skip] no SLUG_MAP entry for: docs/zh-CN/{sub.name}",
                      file=sys.stderr)
                continue
            for md in sorted(sub.glob("*.md")):
                docs.append(_make_doc(md, sub, slug, out, pegasus))

    # --- pegasus/vendor/<vendor>/README*.md + docs/ -----------------------
    vendor_root = pegasus / "vendor"
    if vendor_root.is_dir():
        for vendor in sorted(vendor_root.iterdir()):
            if not vendor.is_dir() or vendor.name not in VENDOR_MAP:
                continue
            slug = VENDOR_MAP[vendor.name]
            # Top-level README → boards/<slug>/index.md
            for md in vendor.glob("README*.md"):
                d = Doc(
                    src=md,
                    dest=out / slug / "index.md",
                    rel_dest=f"{slug}/index.md",
                )
                docs.append(d)
            # vendor/<v>/docs/*.md → boards/<slug>/<filename slug>.md
            sub_docs = vendor / "docs"
            if sub_docs.is_dir():
                for md in sorted(sub_docs.glob("*.md")):
                    fname = _filename_slug(md.stem)
                    d = Doc(
                        src=md,
                        dest=out / slug / f"{fname}.md",
                        rel_dest=f"{slug}/{fname}.md",
                    )
                    docs.append(d)

    # --- pegasus/os/<distro>/README*.md ----------------------------------
    os_root = pegasus / "os"
    if os_root.is_dir():
        for distro in sorted(os_root.iterdir()):
            if not distro.is_dir() or distro.name not in OS_MAP:
                continue
            slug = OS_MAP[distro.name]
            for md in distro.glob("README*.md"):
                # Don't overwrite our hand-written index.md — store as porting.md
                target = "porting.md" if (out / slug / "index.md").exists() else "index.md"
                d = Doc(
                    src=md,
                    dest=out / slug / target,
                    rel_dest=f"{slug}/{target}",
                )
                docs.append(d)

    # --- hi3403-build/README.md → tools/hi3403-build.md ------------------
    if args.hi3403_build:
        hb = Path(args.hi3403_build).resolve()
        readme = hb / "README.md"
        if readme.is_file():
            d = Doc(
                src=readme,
                dest=out / "tools" / "hi3403-build.md",
                rel_dest="tools/hi3403-build.md",
            )
            docs.append(d)

    return docs


def _make_doc(md: Path, src_dir: Path, slug: str, out: Path,
              pegasus: Path) -> Doc:
    """Build a Doc from a single .md file inside a slug-mapped directory."""
    # If a directory maps to a single file, the .md inside is the index.
    # If multi-file (e.g. MPP 13-part), each becomes its own file.
    contents = list(src_dir.glob("*.md"))
    if len(contents) == 1:
        rel_dest = f"{slug}/index.md"
    else:
        # Multi-file: slug each filename
        fname = _filename_slug(md.stem)
        rel_dest = f"{slug}/{fname}.md"
    return Doc(src=md, dest=out / rel_dest, rel_dest=rel_dest)


def _filename_slug(name: str) -> str:
    """
    Make a Chinese / mixed filename URL-safe.
    Strategy: keep ASCII letters, digits, hyphens. Strip everything else.
    Replace whitespace and parens with hyphens. Lowercase.
    Falls back to the H1-derived hash if the result is empty.
    """
    s = name.lower()
    s = s.replace("　", " ")                      # ideographic space
    s = re.sub(r"[（）()【】\[\]｜|\s]+", "-", s)       # punctuation → hyphen
    s = re.sub(r"[^\w\-]", "", s, flags=re.UNICODE)   # keep word/dash
    s = re.sub(r"-+", "-", s).strip("-")
    if not s:
        # Fallback: numeric hash so we never produce an empty path
        import hashlib
        s = "page-" + hashlib.sha1(name.encode()).hexdigest()[:8]
    return s


# --------------------------------------------------------------------------
def collect_image_dirs(src_md: Path) -> List[Path]:
    """Image directories that conventionally live next to a doc."""
    parent = src_md.parent
    candidates = ["figures", "figure", "images", "image",
                  "public_sys-resources", "media", "pic"]
    return [parent / c for c in candidates if (parent / c).is_dir()]


def transform_and_write(doc: Doc, args, summary: List[str]) -> None:
    text = doc.src.read_text(encoding="utf-8", errors="replace")
    title = first_h1(text) or doc.src.stem
    doc.title = title

    text = strip_anchors(text)
    # Add front-matter; mark the source for traceability.
    rel_source = str(doc.src).replace("\\", "/")
    text = inject_front_matter(text, title, rel_source)

    # Skip if already present and not --force
    if doc.dest.exists() and not args.force:
        # Compare content; if identical, skip silently.
        existing = doc.dest.read_text(encoding="utf-8", errors="replace")
        if existing == text:
            summary.append(f"  [unchanged] {doc.rel_dest}")
            return
        else:
            summary.append(f"  [overwrite] {doc.rel_dest}")
    else:
        summary.append(f"  [new]       {doc.rel_dest}")

    if args.dry_run:
        return

    doc.dest.parent.mkdir(parents=True, exist_ok=True)
    doc.dest.write_text(text, encoding="utf-8")

    # Copy images
    if not args.no_images:
        for img_dir in collect_image_dirs(doc.src):
            target = doc.dest.parent / img_dir.name
            if target.exists() and not args.force:
                continue
            shutil.copytree(img_dir, target, dirs_exist_ok=True)


def write_inventory(docs: List[Doc], out: Path) -> None:
    csv_path = out.parent / "inventory.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source", "destination", "title"])
        for d in docs:
            w.writerow([str(d.src), d.rel_dest, d.title])
    print(f"\nInventory written: {csv_path}")


# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pegasus", default="../pegasus",
                    help="Path to the upstream pegasus repo (default ../pegasus)")
    ap.add_argument("--hi3403-build", default="../hi3403-build",
                    help="Path to hi3403-build repo (default ../hi3403-build)")
    ap.add_argument("--out", default="docs",
                    help="Destination root for migrated docs (default ./docs)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="Overwrite existing migrated files even if unchanged")
    ap.add_argument("--no-images", action="store_true")
    args = ap.parse_args()

    out = Path(args.out).resolve()
    print(f"Migration target: {out}")
    print(f"Pegasus source:   {Path(args.pegasus).resolve()}")
    if not Path(args.pegasus).exists():
        print(f"ERROR: pegasus source not found at {args.pegasus}", file=sys.stderr)
        return 2

    docs = discover_docs(args)
    print(f"\nDiscovered {len(docs)} source markdown files.\n")

    summary: List[str] = []
    for d in docs:
        try:
            transform_and_write(d, args, summary)
        except Exception as e:
            summary.append(f"  [ERROR]    {d.rel_dest}: {e}")

    print("\n".join(summary))
    write_inventory(docs, out)

    if not args.dry_run:
        print(f"\nDone. Run `make serve` to preview at "
              f"http://127.0.0.1:8000/")
    else:
        print("\nDry run — no files written.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
