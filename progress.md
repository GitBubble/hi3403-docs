# Translation Progress Report

2026-05-12 (updated evening)

## Current Status

**99% automated — 106K → 1.3K CJK characters across 8 main MPP files.**

| File | Started | Now | Done |
|------|---------|-----|------|
| `13-proc调试信息-131-1315.en.md` | 16,174 | 0 | 100% |
| `03-视频输入.en.md` | 20,113 | 189 | 99% |
| `04-视频输出-41-43.en.md` | 13,584 | 160 | 99% |
| `04-视频输出-44-45.en.md` | 4,746 | 50 | 99% |
| `05-视频处理子系统.en.md` | 16,469 | 241 | 99% |
| `06-视频编码-61-63.en.md` | 16,215 | 234 | 99% |
| `06-视频编码-64-65.en.md` | 10,125 | 189 | 98% |
| `13-proc调试信息-1316-1329.en.md` | 8,353 | 261 | 97% |

52 other .en.md files: zero CJK remaining.

## Toolchain

- `scripts/phrases.py` — 500+ CJK→English phrase mappings in 4 passes
- `scripts/translate.py` — multi-pass translator with `--extract-notes` mode
- `overrides/partials/toc.html` — fixed TOC sidebar (H1-H3 visible)
- `overrides/partials/top.html` — removed (back-to-top fix via CSS)

## Remaining Work

### Script improvement needed: whole-paragraph translation

The current phrase-replacement approach has a fundamental flaw: after stripping CJK characters, English words are concatenated without spaces, producing ugly "Chinglish" like `this interfacecannot be used withothermpiInterfaceSimultaneouslyCalls`. 

The `--extract-notes` mode shows zh/en side by side, but the final pass should:
1. Find paragraphs with CJK in the .en.md file
2. Read the corresponding Chinese paragraph from the .md file
3. Translate the **entire paragraph** as a unit (not word-by-word)
4. Write back clean, properly-spaced English

This would replace the concatenated output with natural prose. The remaining ~1,300 CJK characters are almost entirely in `【注意】` (Note) sections of API descriptions.
