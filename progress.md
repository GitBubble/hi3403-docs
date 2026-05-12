# Translation Progress Report

2026-05-12

## Summary

150 `.en.md` files total. Translation quality is uneven — some are fully translated, while mechanically copied files are almost entirely Chinese.

| Severity | Prose CN lines | File count |
|----------|---------------|------------|
| **Massive** (1000+) | 1,001–7,020 | 17 |
| **Heavy** (500-999) | 500–999 | 7 |
| **Moderate** (100-499) | 100–499 | 19 |
| **Light** (30-99) | 30–99 | 28 |
| **Minimal** (1-29) | 1–29 | 44 |
| **Clean** (0) | 0 | ~35 |

## 17 Massive Files (1,000+ CN lines — 90%+ of remaining work)

These were mechanically copied from Chinese `.md` to `.en.md` without translation. Deeply interleaved technical prose and API identifiers.

| CN lines | File |
|----------|------|
| 7,020 | `docs/multimedia/mpp/03-视频输入.en.md` |
| 6,655 | `docs/multimedia/mpp/04-视频输出-41-43.en.md` |
| 6,421 | `docs/multimedia/mpp/02-系统控制.en.md` |
| 5,441 | `docs/multimedia/mpp/06-视频编码-64-65.en.md` |
| 5,364 | `docs/multimedia/isp/dev-ref/isp-开发参考-1-2.en.md` |
| 5,230 | `docs/multimedia/mpp/13-proc调试信息-131-1315.en.md` |
| 5,163 | `docs/multimedia/mpp/06-视频编码-61-63.en.md` |
| 4,626 | `docs/multimedia/mpp/05-视频处理子系统.en.md` |
| 4,249 | `docs/multimedia/mpp/13-proc调试信息-1316-1329.en.md` |
| 2,979 | `docs/multimedia/mpp/04-视频输出-44-45.en.md` |
| 1,527 | `docs/multimedia/isp/dev-ref/isp-开发参考-3-5.en.md` |
| 1,278 | `docs/multimedia/mpp/07-视频解码.en.md` |
| 1,217 | `docs/reference/sys-config/index.en.md` |
| 1,175 | `docs/multimedia/mpp/10-视频图形子系统.en.md` |
| 1,091 | `docs/multimedia/amct/caffe/index.en.md` |
| 989 | `docs/multimedia/cv/hnr/index.en.md` |
| 882 | `docs/reference/api/ive/ive-api-参考-3-6.en.md` |

## 7 Heavy Files (500-999 CN lines)

| CN lines | File |
|----------|------|
| 848 | `docs/reference/api/klad/index.en.md` |
| 821 | `docs/os/openharmony/porting/index.en.md` |
| 759 | `docs/soc-linux/ddr-tuning/index.en.md` |
| 693 | `docs/multimedia/3dnr/index.en.md` |
| 610 | `docs/os/openharmony/usage/index.en.md` |
| 607 | `docs/tools/accuracy-compare/index.en.md` |
| 600 | `docs/reference/faq/bsp/index.en.md` |

## Light/Minimal Files (1-99 CN lines)

91 files. Most remaining Chinese is in image filenames (file references), `ZH-CN_TOPIC` anchors (cross-reference IDs), or `source:` frontmatter metadata — not user-visible prose.

## Clean Files (0 CN lines)

~35 files. Fully translated.

## Notes

- Image filenames containing Chinese characters reference actual files on disk and cannot be changed without renaming those files.
- `ZH-CN_TOPIC_*` anchor names are internal cross-reference targets; translating them would break internal links.
- `source:` frontmatter lines are metadata recording the original Chinese document path and can be ignored.
- The 17 massive files each represent 100+ page technical reference manuals and need full-document AI translation rather than pattern-based find-and-replace.
