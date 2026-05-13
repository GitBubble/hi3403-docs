# Translation Progress Report

2026-05-13 (final)

## Current Status

**All 56 `.en.md` files in `docs/multimedia/`: zero CJK characters in body text. 83% A/A+ professionalism rating.**

### Professionalism Grades

| Grade | Files | % | Meaning |
|-------|-------|---|---------|
| ⭐ A+ | 46 | 82% | Pristine — no CJK, no concatenation |
| ✅ A | 1 | 2% | Near-perfect — ≤3 minor issues |
| 🟢 B | 2 | 4% | Minor concatenation, passes review |
| 🟡 C | 4 | 7% | Acceptable for reference docs |
| 🔴 D | 3 | 5% | Body-paragraph concatenation |

### D-Grade Files (3)

| File | Runs | Breakdown |
|------|------|-----------|
| `mpp/13-proc调试信息-131-1315.en.md` | 270 | 261 table cells, 9 other |
| `mpp/05-视频处理子系统.en.md` | 79 | 47 bullet, 28 table, 10 other |
| `mpp/06-视频编码-64-65.en.md` | 62 | 12 bullet, 45 table, 12 other |

`13-proc-131-1315` is nearly all table-cell concatenation in parameter reference tables. `05-视频处理子系统` has the most visible body-paragraph issues (47 runs in bullet points).

### C-Grade Files (4)

| File | Runs | Notes |
|------|------|-------|
| `mpp/13-proc调试信息-1316-1329.en.md` | 28 | Mirror of 131-1315, same structure |
| `isp/dev-ref/isp-开发参考-1-2.en.md` | 26 | ISP reference, body text |
| `mpp/03-视频输入.en.md` | 24 | Down from 56; body paragraphs mostly fixed |
| `mpp/06-视频编码-61-63.en.md` | 24 | Down from 152; Notes/Descriptions clean |

### B-Grade Files (2)

`mpp/04-视频输出-44-45.en.md` (8 runs) and `mpp/04-视频输出-41-43.en.md` (5 runs) — nearly pristine after manual paragraph-level retranslation from Chinese source.

### A/A+ Files (47)

All non-MPP content (ISP tuning, graphics, SVP, AMCT, ATC, DIS, HDMI, 3DNR, splash, snapshot, motionfusion, dual-fusion, cv, atc) plus most MPP index/overview pages. Zero issues, production-ready.

## What Was Done

### Automated (previous session)
- `scripts/phrases.py` — 550+ CJK→English phrase mappings, 5 passes
- `scripts/translate.py` — multi-pass translator with deconcat mode
- `scripts/deconcat.py` — CamelCase/acronym splitting
- Result: 106K → ~1,900 CJK characters (98% reduction)

### Manual paragraph-level retranslation (this session)
- `04-视频输出-41-43.en.md` — 30 Description + Note sections retranslated from Chinese `.md` source
- `03-视频输入.en.md` — 10 body paragraphs retranslated
- `06-视频编码-64-65.en.md` — 10 body paragraphs retranslated
- `05-视频处理子系统.en.md` — 9 body paragraphs retranslated
- Word-aware algorithmic deconcatenation pass — 89 additional lines fixed

## Remaining Work

### Manual retranslation (3 D-grade files)
- `13-proc调试信息-131-1315.en.md` — nearly all table cells; low user visibility, skip
- `05-视频处理子系统.en.md` — 47 bullet paragraph runs; worth fixing
- `06-视频编码-64-65.en.md` — 12 bullet paragraph runs; worth fixing

### Body text in C-grade files
- `isp/dev-ref/isp-开发参考-1-2.en.md` — 26 runs, isolated ISP reference sections
- Remaining runs in MPP files are mostly in table cells and acceptable

### Chinese image filenames
~50 image references like `![](figures/VENC的数据流程图.png)` — filenames reference actual PNG files on disk. Requires file rename + link update.

## Approach That Works

For each concatenated paragraph:
1. Read garbled English in `.en.md` file
2. Cross-reference Chinese source in `.md` file (same line offset)
3. Translate Chinese paragraph as a whole unit
4. Replace with Edit tool

Pattern matching (sed/Python string replace) is ineffective — each concatenated sentence is unique. Paragraph-level translation from Chinese source is the only reliable method.
