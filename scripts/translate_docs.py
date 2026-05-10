#!/usr/bin/env python3
"""Generate English *.en.md siblings from Chinese markdown pages.

This is a content-generation helper for the MkDocs static i18n setup.
It preserves front matter, fenced code blocks, URLs and markdown structure
well enough for doc-site generation, while translating visible prose.

Requires:
  pip install deep-translator python-frontmatter
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path
from typing import Iterable

import frontmatter
from deep_translator import GoogleTranslator

CHINESE_RE = re.compile(r"[\u3400-\u9fff]")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")
ADMONITION_RE = re.compile(r'^(\s*)([!?]{3}\+?\s+[A-Za-z_-]+)(?:\s+"([^"]*)")?(\s*)$')
MARKER_RE = re.compile(r'^(\s*(?:#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s+))(.*)$')
FENCE_BLOCK_RE = re.compile(r"(?ms)^(```|~~~)([^\n]*)\n(.*?)(^\1\s*$)")
LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\(([^)]+)\)')
INLINE_CODE_RE = re.compile(r'`[^`\n]+`')
HTML_TAG_RE = re.compile(r'</?[^>]+?>')
RAW_URL_RE = re.compile(r'https?://[^\s)>"]+')
TOKEN_PREFIX = "ZXTOKEN"
TRANSLATABLE_FENCE_LANGS = {"", "text", "txt", "plain"}
MERMAID_LABEL_RE = re.compile(r'\[([^\]\n]*[\u3400-\u9fff][^\]\n]*)\]')
MERMAID_QUOTED_RE = re.compile(r'"([^"\n]*[\u3400-\u9fff][^"\n]*)"')
EXACT_OVERRIDES = {
    "首页": "Home",
    "快速开始": "Get started",
    "快速启动": "Quick start",
    "选择开发板": "Choose a development board",
    "选择操作系统": "Choose an operating system",
    "安装开发环境": "Set up the development environment",
    "安装 SDK": "Install the SDK",
    "驱动安装": "Driver installation",
    "上游 SDK 快速开始": "Upstream SDK quick start",
    "开发板": "Boards",
    "操作系统": "OS",
    "概览": "Overview",
    "移植": "Porting",
    "使用": "Usage",
    "SoC 与 Linux": "SoC & Linux",
    "多媒体与 AI": "Multimedia & AI",
    "工具": "Tools",
    "参考": "Reference",
    "教程": "Tutorials",
    "社区": "Community",
    "准备": "Preparation",
    "接线": "Wiring",
    "烧录镜像": "Flash the image",
    "厂商镜像": "Vendor-provided images",
    "自己构建": "Build it yourself",
    "上电登录": "Power on and log in",
    "主机开发环境": "Host development environment",
    "接下来": "Next",
    "板子对比": "Board comparison",
    "系统对比": "OS comparison",
    "Ubuntu 构建指南": "Ubuntu build guide",
    "开发环境": "Development environment",
    "SDK 安装": "SDK installation",
    "板子": "Board",
    "厂商": "Vendor",
    "系统": "OS",
    "选项": "Options",
    "详细": "Details",
    "文档": "Document",
    "介质": "Medium",
    "采集编码": "Capture and encode",
    "采集编码教程": "Capture and encode tutorial",
    "ISP 调色": "ISP color tuning",
    "ISP 调色教程": "ISP color tuning tutorial",
    "SVP 首次推理": "First SVP inference",
    "NPU 推理 (YOLO)": "NPU inference (YOLO)",
    "摄像头采集 + H.264 编码": "Camera capture + H.264 encoding",
    "ISP / 白平衡": "ISP / white balance",
    "完整 SDK 流程": "Full SDK workflow",
    "构建脚本参数": "Build script parameters",
    "安全启动": "Secure Boot",
    "外设驱动": "Peripheral Drivers",
    "内存布局": "Memory Layout",
    "DDR 调优": "DDR Tuning",
    "PCIE 级联": "PCIe Cascading",
    "安全子系统": "Security Subsystem",
    "应用开发": "Application Development",
    "开发指南": "Developer Guide",
    "开发参考": "Developer Reference",
    "调优": "Tuning",
    "颜色管理": "Color Management",
    "传感器适配": "Sensor Adaptation",
    "计算机视觉": "Computer Vision",
    "抓拍": "Snapshot",
    "黑白彩色双路融合": "Dual-stream Mono/Color Fusion",
}


class Translator:
    """Caches translations on disk so a long run can resume.

    The cache lives at scripts/.translate_cache.json by default.
    Set HI3403_TRANSLATE_CACHE to override.
    """

    def __init__(self, source: str = "zh-CN", target: str = "en",
                 cache_path: str | None = None) -> None:
        import json
        self.engine = GoogleTranslator(source=source, target=target)
        self.cache_path = cache_path or str(
            Path(__file__).parent / ".translate_cache.json")
        self.cache: dict[str, str] = {}
        try:
            with open(self.cache_path, "r", encoding="utf-8") as f:
                self.cache = json.load(f)
        except FileNotFoundError:
            pass
        except Exception as exc:
            print(f"WARN: could not load cache {self.cache_path}: {exc}")
        self._writes_since_flush = 0

    def _flush(self) -> None:
        import json
        try:
            with open(self.cache_path, "w", encoding="utf-8") as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=0)
        except Exception as exc:
            print(f"WARN: could not save cache: {exc}")

    def translate(self, text: str) -> str:
        if not text or not CHINESE_RE.search(text):
            return text
        cached = self.cache.get(text)
        if cached is not None:
            return cached
        for attempt in range(3):
            try:
                out = self.engine.translate(text)
                self.cache[text] = out
                self._writes_since_flush += 1
                # Flush every 50 new entries so an interrupted run keeps progress.
                if self._writes_since_flush >= 50:
                    self._flush()
                    self._writes_since_flush = 0
                return out
            except Exception:
                if attempt == 2:
                    self.cache[text] = text
                    return text
                time.sleep(0.5 * (attempt + 1))
        return text

    def close(self) -> None:
        if self._writes_since_flush:
            self._flush()


def has_chinese(text: str) -> bool:
    return bool(CHINESE_RE.search(text))


def mask_pattern(text: str, pattern: re.Pattern[str], store: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        token = f"{TOKEN_PREFIX}{len(store)}END"
        store[token] = match.group(0)
        return token

    return pattern.sub(repl, text)


def restore_tokens(text: str, store: dict[str, str]) -> str:
    for token, value in store.items():
        text = text.replace(token, value)
    return text


def translate_inline(text: str, tr: Translator) -> str:
    if not has_chinese(text):
        return text

    leading_len = len(text) - len(text.lstrip())
    leading = text[:leading_len]
    body = text[leading_len:]
    trailing_len = len(body) - len(body.rstrip())
    if trailing_len:
        trailing = body[-trailing_len:]
        body = body[:-trailing_len]
    else:
        trailing = ""

    if body in EXACT_OVERRIDES:
        return leading + EXACT_OVERRIDES[body] + trailing

    placeholders: dict[str, str] = {}

    def repl_link(match: re.Match[str]) -> str:
        bang, label, url = match.groups()
        translated_label = translate_inline(label, tr) if has_chinese(label) else label
        token = f"{TOKEN_PREFIX}{len(placeholders)}END"
        placeholders[token] = f"{bang}[{translated_label}]({url})"
        return token

    body = LINK_RE.sub(repl_link, body)
    body = mask_pattern(body, INLINE_CODE_RE, placeholders)
    body = mask_pattern(body, RAW_URL_RE, placeholders)
    body = mask_pattern(body, HTML_TAG_RE, placeholders)

    if has_chinese(body):
        body = tr.translate(body)

    return leading + restore_tokens(body, placeholders) + trailing


def translate_table_line(line: str, tr: Translator) -> str:
    stripped = line.strip()
    if not stripped or TABLE_SEP_RE.match(line):
        return line

    prefix = line[: len(line) - len(line.lstrip())]
    core = stripped
    leading = core.startswith("|")
    trailing = core.endswith("|")
    cells = core.strip("|").split("|")
    translated = [translate_inline(cell.strip(), tr) for cell in cells]
    body = " | ".join(translated)
    if leading:
        body = "| " + body
    if trailing:
        body = body + " |"
    return prefix + body


def translate_line(line: str, tr: Translator) -> str:
    if not has_chinese(line):
        return line
    if TABLE_SEP_RE.match(line):
        return line

    admonition = ADMONITION_RE.match(line)
    if admonition:
        indent, head, title, tail = admonition.groups()
        if title:
            return f'{indent}{head} "{translate_inline(title, tr)}"{tail}'
        return line

    if "|" in line and line.count("|") >= 2:
        return translate_table_line(line, tr)

    marker = MARKER_RE.match(line)
    if marker:
        prefix, body = marker.groups()
        return prefix + translate_inline(body, tr)

    return translate_inline(line, tr)


def translate_text_block(text: str, tr: Translator) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    for line in lines:
        newline = ""
        if line.endswith("\r\n"):
            content = line[:-2]
            newline = "\r\n"
        elif line.endswith("\n"):
            content = line[:-1]
            newline = "\n"
        else:
            content = line
        out.append(translate_line(content, tr) + newline)
    return "".join(out)


def translate_mermaid_block(text: str, tr: Translator) -> str:
    def repl_label(match: re.Match[str]) -> str:
        return "[" + translate_inline(match.group(1), tr) + "]"

    def repl_quoted(match: re.Match[str]) -> str:
        return '"' + translate_inline(match.group(1), tr) + '"'

    text = MERMAID_LABEL_RE.sub(repl_label, text)
    text = MERMAID_QUOTED_RE.sub(repl_quoted, text)
    return text


def translate_body(text: str, tr: Translator) -> str:
    parts: list[str] = []
    last = 0
    for match in FENCE_BLOCK_RE.finditer(text):
        parts.append(translate_text_block(text[last: match.start()], tr))
        fence, info, body, close = match.groups()
        lang = info.strip().split()[0].lower() if info.strip() else ""
        if lang in TRANSLATABLE_FENCE_LANGS:
            body = translate_text_block(body, tr)
        elif lang == "mermaid":
            body = translate_mermaid_block(body, tr)
        parts.append(f"{fence}{info}\n{body}{close}")
        last = match.end()
    parts.append(translate_text_block(text[last:], tr))
    return "".join(parts)


def translate_metadata(value, tr: Translator, key: str | None = None):
    if isinstance(value, dict):
        return {k: translate_metadata(v, tr, k) for k, v in value.items()}
    if isinstance(value, list):
        return [translate_metadata(v, tr, key) for v in value]
    if isinstance(value, str):
        if key in {"source", "edit_uri", "url", "link"}:
            return value
        return translate_inline(value, tr)
    return value


def english_path(path: Path) -> Path:
    if path.name.endswith(".en.md"):
        return path
    return path.with_name(path.stem + ".en.md")


def iter_base_docs(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if path.name.endswith(".en.md"):
            continue
        yield path


def translate_file(path: Path, tr: Translator, force: bool) -> Path:
    target = english_path(path)
    if target.exists() and not force:
        return target

    post = frontmatter.loads(path.read_text(encoding="utf-8"))
    translated_meta = {
        key: translate_metadata(value, tr, key)
        for key, value in post.metadata.items()
    }
    translated_body = translate_body(post.content, tr)
    out = frontmatter.Post(translated_body, **translated_meta)
    target.write_text(frontmatter.dumps(out), encoding="utf-8")
    return target


def nav_labels_from_mkdocs(text: str) -> list[str]:
    labels: list[str] = []
    in_nav = False
    for line in text.splitlines():
        if line.startswith("nav:"):
            in_nav = True
            continue
        if in_nav:
            if re.match(r"^[^\s#]", line):
                break
            match = re.match(r"^\s*-\s+(.+?):(?:\s+.*)?$", line)
            if match:
                labels.append(match.group(1))
    deduped: list[str] = []
    seen: set[str] = set()
    for label in labels:
        if label not in seen:
            seen.add(label)
            deduped.append(label)
    return deduped


def build_nav_translation_block(labels: list[str], tr: Translator) -> str:
    lines = []
    for label in labels:
        translated = EXACT_OVERRIDES.get(label) or translate_inline(label, tr)
        translated = translated.replace('"', '\\"')
        lines.append(f'            "{label}": "{translated}"')
    return "\n".join(lines)


def update_mkdocs_yml(mkdocs_path: Path, tr: Translator) -> None:
    text = mkdocs_path.read_text(encoding="utf-8")

    if "reconfigure_material: true" not in text:
        marker = "  - i18n:\n"
        if marker not in text:
            raise SystemExit("Could not locate i18n plugin in mkdocs.yml")
        text = text.replace(marker, marker + "      reconfigure_material: true\n", 1)

    labels = nav_labels_from_mkdocs(text)
    block = build_nav_translation_block(labels, tr)
    pattern = re.compile(r"(?ms)(\n\s{10}nav_translations:\n)(.*?)(\n\s{2}-\s+tags)")
    match = pattern.search(text)
    if not match:
        raise SystemExit("Could not locate nav_translations block in mkdocs.yml")
    text = text[: match.start()] + match.group(1) + block + match.group(3) + text[match.end():]
    mkdocs_path.write_text(text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate Chinese .md pages to .en.md siblings.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Common workflows:

  # Translate everything that doesn't yet have an .en.md sibling:
  python3 scripts/translate_docs.py

  # Force-retranslate everything (re-uses on-disk cache so stable
  # phrases are still cheap):
  python3 scripts/translate_docs.py --force

  # Translate a subset (useful after editing a few pages):
  python3 scripts/translate_docs.py --only docs/get-started docs/multimedia/mpp

  # Translate at most N files this run (resumable):
  python3 scripts/translate_docs.py --max-files 20

  # Plus update mkdocs.yml nav_translations:
  python3 scripts/translate_docs.py --update-mkdocs
""")
    parser.add_argument("--docs-root", default="docs")
    parser.add_argument("--only", nargs="*",
                        help="Limit to these files / directories")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing .en.md files")
    parser.add_argument("--max-files", type=int, default=0,
                        help="Translate at most this many files this run "
                             "(0 = no limit)")
    parser.add_argument("--update-mkdocs", action="store_true",
                        help="Also rewrite the nav_translations block in mkdocs.yml")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.docs_root)
    tr = Translator()

    if args.only:
        paths = []
        for item in args.only:
            path = Path(item)
            if path.is_dir():
                paths.extend(iter_base_docs(path))
            else:
                paths.append(path)
    else:
        paths = list(iter_base_docs(root))

    # Skip already-translated unless --force.
    if not args.force:
        paths = [p for p in paths if not english_path(p).exists()]

    if args.max_files > 0:
        paths = paths[: args.max_files]

    written = []
    total = len(paths)
    for i, path in enumerate(paths, 1):
        if path.name.endswith(".en.md"):
            continue
        print(f"[{i}/{total}] {path}")
        try:
            written.append(translate_file(path, tr, force=args.force))
        except Exception as exc:
            print(f"  ERROR: {exc}")

    tr.close()

    if args.update_mkdocs:
        update_mkdocs_yml(Path("mkdocs.yml"), tr)

    print(f"translated_files={len(written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
