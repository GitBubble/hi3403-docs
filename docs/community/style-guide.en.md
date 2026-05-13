---
description: Hi3403 document writing conventions
title: style guide
--- # style guide This is the convention when writing Hi3403 documentation. Goal: All pages read in a consistent, professional, and
Friendly to new readers. ## Tone - **Direct, eye level**. No "we" / "I" / "you" / "please".
- **objective**. "Better performance" requires data; "recommendation" requires reasons.
- **No selling out**. Put the conclusion in the first paragraph. | don't want | want |
|---|---|
| "Dear developers, welcome to SVP!" | "SVP is the NPU of Hi3403. This section introduces its development model." |
| "You can modify it as needed" | "Can be modified" |
| "For a better experience, we recommend that you..." | "suggestion..." | ## structure Standard structure of each page: ```
---
title: short title
description: one sentence description (will be displayed in the search results)
--- # title An introduction: What is this page about and what can you do after reading it. ## Second level title text. ## Second level title text. ## Next Jump to the next card grid.
``` Page length should be within **5–10 screens**. Extra long ones are split into multiple pages. ## Title level - `#` - only appears once at the beginning of the file (page title)
- `##` - main paragraph
- `###` - subparagraph
- `####` - rarely used Do not skip levels (`#` jumps directly to `###`). ## Link **Use relative paths** to link to other pages on this site: ```markdown
[ISP Tuning](../multimedia/isp/tuning/index.md) ✓ correct
[ISP Tuning](https:/docs.example.com/multimedia/...) ✗ wrong
``` External links remain https. **Don't** add "(opens in new tab)" to https links.
Note - The browser will handle this on its own. ## code block Always give language tags: ````markdown
``` bash
make build
```
```` Do not write bare ` ``` `. Command-line examples **without a prompt** (`$` `#`) — easier to copy-paste: | Don't | Do |
|---|---|
| `$ make build` | `make build` |
| `# apt update` | `sudo apt update` | When distinguishing user/root is necessary, write `sudo` explicitly. ## Command output Put expected output in a separate code block, not mixed into the command: ````markdown
``` bash
make verify
``` Expected output: ```
✓ All 5 downloads verified
```
```` ## Admonition blocks Use the admonitions provided by the Material theme: ```markdown
!!! note "Title (optional)" This is a note. !!! warning This is a warning.
``` Available types: `note`, `tip`, `info`, `warning`, `danger`, `example`,
`question`, `bug`. ## card grid Each section landing uses grid cards: ```markdown
<div class="grid cards" markdown> - :material-rocket-launch:{ .lg .middle } __Title__ --- One-line description. [:octicons-arrow-right-24: Go](path/to/page.md) </div>
``` The icon uses [Material Icons](https:/pictogrammers.github.io/@mdi/font/2.0.46/) or
Octicons/Simple Icons. Try to unify the icon family within a section. ## sheet Use pipe tables, not HTML: ```markdown
| Col 1 | Col 2 |
|---|---|
| Val 1 | Val 2 |
``` If markdown cannot support complex tables, change it to admonition + multiple tables. ## picture Place it in a subdirectory of the same name on each page: ```
docs/
└── multimedia/ └── isp/ ├── tuning.md └── images/ └── awb-flow.png
``` Quote: `ZXTOKEN0END` Add `alt` text (Accessibility + SEO). ## Chinese and English - **Add spaces between CJK and Latin characters**: `Uses ATC has`, not `Uses AT Chas` (for Chinese-language pages)
- **Numbers, units, English punctuation**: use half-width, add spaces before and after - `8 GB`, `30 fps`, `5.5 V`
- **Use Chinese punctuation in Chinese**: `，。：；！？` - not `,.;!?`
- Use backticks when quoting code, file names, and variables: \`isp_awb.cfg\` ## abbreviation Add the full name when it first appears: ```
ISP (Image Signal Processor, image signal processor) is responsible for...
``` You can then just use the abbreviation. The full title does not need to be repeated in the "next" or "reference" paragraphs on each page. [Glossary](../reference/glossary.md) has unified definitions for all abbreviations - when writing new abbreviations
Check the table first to avoid disagreements. ## don't want - ❌ Emojis everywhere — occasionally using ✓ ✗ in titles for status is acceptable; use sparingly in body text
- ❌ "More efficient" / "faster" without giving a baseline
- ❌ Put a lot of code in a long paragraph - split it into short paragraphs + code blocks
- ❌ Translation accent ("As you can see..." → "As you can see...") ## proofreading checklist Go through this before submitting a PR: - [ ] Is the title level reasonable (no level skipping)
- [ ] Use relative paths for internal links
- [ ] Code blocks have language tags
- [ ] There is a space between Chinese and English
- [ ] The full name is given the first time an abbreviation appears.
- [ ] ran `make serve` and saw the effect locally.
- [ ] (ideal situation) `make linkcheck` ran without breaking the link