#!/usr/bin/env python3
"""Translate remaining Chinese in .en.md files using Google Translate.

This is a patch-mode translator for existing .en.md files that still contain
Chinese text. It reuses the structure-preserving pipeline from translate_docs.py
(HTML tags, code fences, links, inline code, tables) with the same Google
Translate engine, but patches files in-place rather than creating new ones.

Requires:
  pip install deep-translator python-frontmatter
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Iterable

from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator

# ── Pattern constants (shared with translate_docs.py) ──────────────────────

CHINESE_RE = re.compile(r"[㐀-鿿]")
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
MERMAID_LABEL_RE = re.compile(r'\[([^\]\n]*[㐀-鿿][^\]\n]*)\]')
MERMAID_QUOTED_RE = re.compile(r'"([^"\n]*[㐀-鿿][^"\n]*)"')

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
    "数据类型": "Data Types",
}

DEFAULT_TARGETS = [
    "docs/multimedia/mpp/02-系统控制.en.md",
    "docs/multimedia/mpp/03-视频输入.en.md",
    "docs/multimedia/mpp/04-视频输出-41-43.en.md",
    "docs/multimedia/mpp/04-视频输出-44-45.en.md",
    "docs/multimedia/mpp/05-视频处理子系统.en.md",
    "docs/multimedia/mpp/06-视频编码-61-63.en.md",
    "docs/multimedia/mpp/06-视频编码-64-65.en.md",
    "docs/multimedia/mpp/13-proc调试信息-131-1315.en.md",
    "docs/multimedia/mpp/13-proc调试信息-1316-1329.en.md",
    "docs/multimedia/isp/dev-ref/isp-开发参考-1-2.en.md",
]


# ── Translator with cache (same pattern as translate_docs.py) ───────────

class Translator:
    """Google Translate wrapper with on-disk cache."""

    def __init__(self, source: str = "zh-CN", target: str = "en",
                 cache_path: str | None = None) -> None:
        self.engine = GoogleTranslator(source=source, target=target)
        self.cache_path = cache_path or str(
            Path(__file__).parent / ".translate_patch_cache.json")
        self.cache: dict[str, str] = {}
        try:
            with open(self.cache_path, "r", encoding="utf-8") as f:
                self.cache = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        except Exception as exc:
            print(f"  WARN: could not load cache: {exc}")
        self._writes_since_flush = 0

    def _flush(self) -> None:
        try:
            with open(self.cache_path, "w", encoding="utf-8") as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=0)
        except Exception as exc:
            print(f"  WARN: could not save cache: {exc}")

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

    def translate_parallel(self, texts: list[str], workers: int = 4) -> list[str]:
        """Translate a list of texts in parallel."""
        results: dict[str, str] = {}
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futures = {ex.submit(self.translate, t): t for t in texts}
            for f in as_completed(futures):
                results[futures[f]] = f.result()
        return [results.get(t, t) for t in texts]


# ── Structure-preserving translation helpers ─────────────────────────────

def has_chinese(text: str) -> bool:
    return bool(CHINESE_RE.search(text))


def mask_pattern(text: str, pattern: re.Pattern[str],
                 store: dict[str, str]) -> str:
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
        translated_label = (translate_inline(label, tr)
                            if has_chinese(label) else label)
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
        if title and has_chinese(title):
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
    """Translate text with batching + parallel API calls."""
    raw_lines = text.splitlines(keepends=True)

    def nl(line: str) -> str:
        return "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""

    MAX_BATCH = 50
    # Collect all batches first, then translate in parallel
    batches: list[tuple[str, list[str], list[int]]] = []  # (joined, prefixes, indices)
    batch_bodies: list[str] = []
    batch_prefixes: list[str] = []
    batch_indices: list[int] = []
    line_tokens: list[str | None] = [None] * len(raw_lines)  # None=must process inline

    seen = 0
    for i, line in enumerate(raw_lines):
        if seen > i:
            continue
        if not has_chinese(line) or TABLE_SEP_RE.match(line.strip()):
            line_tokens[i] = line
            continue

        # Table lines — individual treatment (skip, handled later)
        if "|" in line and line.count("|") >= 2:
            line_tokens[i] = None  # will inline-process
            continue

        admonition = ADMONITION_RE.match(line.strip())
        if admonition:
            line_tokens[i] = None  # will inline-process
            continue

        # Accumulate batch
        batch_bodies.clear()
        batch_prefixes.clear()
        batch_indices.clear()
        j = i
        while j < len(raw_lines) and len(batch_bodies) < MAX_BATCH:
            ln = raw_lines[j]
            if not has_chinese(ln):
                break
            s = ln.strip()
            if TABLE_SEP_RE.match(s) or (s and "|" in ln and ln.count("|") >= 2):
                break
            if ADMONITION_RE.match(s):
                break
            marker = MARKER_RE.match(s)
            if marker:
                pfx, body = marker.groups()
                batch_prefixes.append(pfx)
                batch_bodies.append(body)
            else:
                batch_prefixes.append("")
                batch_bodies.append(s)
            batch_indices.append(j)
            j += 1

        if batch_bodies:
            joined = "\n".join(batch_bodies)
            batches.append((joined, list(batch_prefixes), list(batch_indices)))
            for bi in batch_indices:
                line_tokens[bi] = f"__BATCH_{len(batches)-1}__"
            seen = j
        else:
            line_tokens[i] = line

    # Translate all batches in parallel
    if batches:
        batch_texts = [b[0] for b in batches]
        batch_results = tr.translate_parallel(batch_texts)

        # Store translated lines per batch
        for bi, (_, prefixes, indices) in enumerate(batches):
            translated = batch_results[bi] if bi < len(batch_results) else ""
            tlines = translated.split("\n") if translated else []
            for tj, tl in enumerate(tlines):
                if tj < len(indices):
                    si = indices[tj]
                    pfx = prefixes[tj] if tj < len(prefixes) else ""
                    line_tokens[si] = f"{pfx}{tl.strip()}{nl(raw_lines[si])}"

    # Assemble output: inline-process table lines and admonitions
    out: list[str] = []
    for i, line in enumerate(raw_lines):
        if line_tokens[i] is not None:
            out.append(line_tokens[i])
        elif "|" in line and line.count("|") >= 2 and has_chinese(line):
            content = line.rstrip("\n\r")
            out.append(translate_table_line(content, tr) + nl(line))
        elif ADMONITION_RE.match(line.strip()):
            m = ADMONITION_RE.match(line.strip())
            _, head, title, tail = m.groups()
            if title and has_chinese(title):
                out.append(f'{head} "{translate_inline(title, tr)}"{tail}\n')
            else:
                out.append(line)
        else:
            out.append(line)

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
    if not has_chinese(text):
        return text
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


def count_chinese(text: str) -> int:
    return len(CHINESE_RE.findall(text))


# ── File patching ─────────────────────────────────────────────────────────

def patch_file(path: Path, tr: Translator,
              backup: bool = True,
              force: bool = False) -> dict:
    """Translate remaining Chinese in an existing .en.md file.

    Returns {'path': ..., 'before': N, 'after': M, 'status': ...}.
    """
    if not path.exists():
        return {"path": str(path), "before": 0, "after": 0,
                "status": "not_found"}

    content = path.read_text(encoding="utf-8")
    before = count_chinese(content)

    if before == 0:
        return {"path": str(path), "before": 0, "after": 0,
                "status": "clean"}

    if backup:
        backup_path = path.with_suffix(path.suffix + ".bak")
        backup_path.write_text(content, encoding="utf-8")

    # Split frontmatter from body
    parts = content.split("---", 2)
    if len(parts) >= 3:
        fm_raw = "---".join(parts[:2]) + "---"
        body_raw = parts[2]
    else:
        fm_raw = ""
        body_raw = content

    # Translate body
    translated_body = translate_body(body_raw, tr)

    # Only re-translate frontmatter title if it contains Chinese
    translated_fm = fm_raw
    if has_chinese(fm_raw):
        title_match = re.search(r'^title:\s*"([^"]*)"', fm_raw, re.MULTILINE)
        if title_match and has_chinese(title_match.group(1)):
            new_title = translate_inline(title_match.group(1), tr)
            translated_fm = fm_raw.replace(
                f'"{title_match.group(1)}"', f'"{new_title}"', 1)

    result = translated_fm + "\n" + translated_body if fm_raw else translated_body
    after = count_chinese(result)

    if not force and after >= before:
        return {"path": str(path), "before": before, "after": after,
                "status": "unchanged"}

    path.write_text(result, encoding="utf-8")
    status = "clean" if after == 0 else "partial"
    return {"path": str(path), "before": before, "after": after,
            "status": status}


# ── CLI ───────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate remaining Chinese in .en.md files using Google Translate.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:

  # Patch all known MPP/ISP files (default):
  python3 scripts/translate_deepl.py

  # Dry run (audit only, no changes):
  python3 scripts/translate_deepl.py --dry-run

  # Patch specific files:
  python3 scripts/translate_deepl.py --files path/to/file.en.md

  # Force re-translate even if Chinese didn't drop:
  python3 scripts/translate_deepl.py --force
""")
    parser.add_argument("--files", nargs="*",
                        help="Specific .en.md files to patch")
    parser.add_argument("--dry-run", action="store_true",
                        help="Audit only, no changes written")
    parser.add_argument("--no-backup", action="store_true",
                        help="Skip .bak backup")
    parser.add_argument("--force", action="store_true",
                        help="Re-translate even if Chinese count didn't drop")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    tr = None if args.dry_run else Translator()

    # Resolve target files
    if args.files:
        paths = [Path(p) for p in args.files]
    else:
        root = Path(__file__).parent.parent
        paths = [root / p for p in DEFAULT_TARGETS]

    results = []
    for path in paths:
        if tr is None:
            before = count_chinese(path.read_text(encoding="utf-8"))
            results.append({
                "path": str(path), "before": before,
                "after": before, "status": "dry_run"
            })
            continue

        result = patch_file(path, tr,
                            backup=not args.no_backup,
                            force=args.force)
        results.append(result)

    if tr is not None:
        tr.close()

    # Summary
    total_before = sum(r["before"] for r in results)
    total_after = sum(r["after"] for r in results)
    clean = sum(1 for r in results if r["status"] == "clean")
    partial = sum(1 for r in results if r["status"] == "partial")
    errors = sum(1 for r in results if r["status"] == "not_found")

    print(f"\n{'=' * 60}")
    print(f"Results: {len(results)} files")
    for r in results:
        short = r["path"]
        if len(short) > 60:
            short = "..." + short[-57:]
        if r["status"] == "not_found":
            print(f"  [x] {short} — not found")
        elif r["status"] == "dry_run":
            print(f"  [~] {short} — {r['before']} CN chars (dry run)")
        elif r["status"] == "clean":
            print(f"  [OK] {short} — clean")
        elif r["status"] == "unchanged":
            print(f"  [-] {short} — unchanged ({r['before']}->{r['after']})")
        elif r["after"] == 0:
            print(f"  [OK] {short} — {r['before']}->0 CN chars")
        else:
            print(f"  [..] {short} — {r['before']}->{r['after']} CN chars")

    print(f"\nTotal: {total_before} -> {total_after} Chinese chars "
          f"({total_before - total_after} translated)")
    print(f"Clean: {clean}, Partial: {partial}, Not found: {errors}")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
