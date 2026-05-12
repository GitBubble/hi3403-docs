# Hi3403 Developer Center

The community documentation site for the HiSilicon **Hi3403V100 / Hi3519AV200
Hi3403** platform


> Source for the site published at *(deploy URL TBD)*. Built with MkDocs +
> the Material theme.

```
hi3403-docs/
├── docs/                      # All documentation source (Markdown)
│   ├── index.md               # Homepage card grid
│   ├── get-started/           # 1. Get started
│   ├── boards/                # 2. Boards
│   ├── os/                    # 3. Operating systems
│   ├── soc-linux/             # 4. SoC & Linux
│   ├── multimedia/            # 5. Multimedia & AI
│   ├── tools/                 # 6. Tools
│   ├── reference/             # 7. Reference
│   └── community/             # Contribution & licensing
├── overrides/                 # Small theme template tweaks
├── scripts/                   # Migration + maintenance scripts
├── .github/workflows/         # CI: build + deploy to Pages
├── mkdocs.yml                 # Site configuration
├── Makefile                   # Build verbs (`make`, `make serve`, `make migrate`)
├── requirements.txt           # Python dependencies
├── LICENSE                    # CC BY-SA 4.0 for content / BSD-3 for tooling
└── README.md
```

## Quick start (for editors)

```bash
make install     # one-time: pip install -r requirements.txt
make serve       # live-preview at http://127.0.0.1:8000/
```

Edit any file under `docs/`, save it, and the preview reloads.

## Build verbs

| Command | What it does |
|---|---|
| `make` (default) | Build the static site to `site/` |
| `make serve` | Live-preview server at <http://127.0.0.1:8000/> |
| `make serve_html` | Same as `serve` (matches RPi naming) |
| `make migrate` | Re-run `scripts/migrate.py` to ingest source docs from `../hi3403/` |
| `make linkcheck` | Offline link check |
| `make lint` | Markdownlint pass |
| `make clean` | Delete `site/` and build cache |

## Information architecture

Seven top-level sections (rendered as nav tabs, RPi-style):

| # | Section | What lives here |
|---|---|---|
| 1 | **Get started** | Quickstart, board picker, OS picker, environment setup |
| 2 | **Boards** | One landing page per supported board (Topeet, LubanCat, Euler Pi, …) |
| 3 | **OS** | Per-distro porting & usage (Ubuntu, OpenHarmony, OpenEuler, Buildroot) |
| 4 | **SoC & Linux** | Chip docs, U-Boot, kernel, drivers, peripherals, secure boot, memory |
| 5 | **Multimedia & AI** | MPP, ISP, codecs, audio, SVP/ATC, IVE/IVS/DPU/HNR, MotionFusion |
| 6 | **Tools** | hi3403-build, BurnTool, MindCmd, ToolPlatform, profiling tools |
| 7 | **Reference** | API references, FAQs, SYS_CONFIG, glossary |

A **Community** tab in the side navigation hosts release notes,
contribution guide, style guide, and license.

## Languages

- **zh-CN** is the primary language (all upstream hi3403 content is
  Chinese). Default URL: `/`.
- **English** scaffolding is in place (`docs/en/`). Pages exist as stubs
  and will be filled in as community contributors translate them.

## Migration from upstream hi3403

`scripts/migrate.py` ingests the existing `hi3403/` documentation
(95 files in `docs/zh-CN/`, plus per-vendor docs) into this repo:

1. Maps each upstream path to a slug-friendly destination.
2. Strips generated HTML anchors (`<a name="ZH-CN_TOPIC_..."></a>`).
3. Adds YAML front-matter (title, source).
4. Copies images alongside their parent doc.
5. Rewrites internal links per the rename map.

Run `make migrate` from this directory to re-ingest after the upstream
repo updates.

## Contributing

See [`docs/community/contributing.md`](docs/community/contributing.md)
and [`docs/community/style-guide.md`](docs/community/style-guide.md).

## License

- **Documentation** (`docs/`): CC BY-SA 4.0
- **Tooling** (everything else): BSD 3-Clause

See [`LICENSE`](./LICENSE) for the full text.

## Note on repo location

This repo currently lives inside `hi3403-build/hi3403-docs/` because
of the workspace layout it was created in. Once you're ready to publish
it, move the directory to a sibling of `hi3403-build/`:

```bash
mv hi3403-build/hi3403-docs ./hi3403-docs
cd hi3403-docs
git init && git add -A && git commit -m "Initial commit"
```
