---
description: 'A step-by-step guide: Clone → Write a page → Preview locally → Submit
  a PR'
title: Add a new page
---

# Add a new page

This article is a step-by-step tutorial for contributors who are adding pages to the Hi3403 documentation for the first time.
Follow along for about 15 minutes.

## Decide where to go

Each page corresponds to a specific location in IA. The following are the directories corresponding to the 7 sections:

| Section | Table of contents | What to pretend |
|---|---|---|
| Get Started | `docs/get-started/` | Quickstart, decision, installation |
| Boards | `docs/boards/<vendor>/` | Board-specific content |
| OS | `docs/os/<distro>/` | OS porting, distro-specific content |
| SoC & Linux | `docs/soc-linux/` | Chip + kernel + boot related |
| Multimedia & AI | `docs/multimedia/` | MPP, ISP, AI |
| Tools | `docs/tools/` | Tools |
| Reference | `docs/reference/` | API, FAQ, configuration |
| Tutorials | `docs/tutorials/` | End-to-end practice |
| Community | `docs/community/` | Process class |

**Example**: You wrote a tutorial on "Running GStreamer on Hi3403". This is end-to-end actual combat,
So put `docs/tutorials/gstreamer.md`.

## Step 1 — Create the file

``` bash
cd hi3403-docs
$EDITOR docs/tutorials/gstreamer.md
```

## Step 2 — Add front-matter

YAML front-matter is required at the top of every page:

``` markdown
---
title: Running GStreamer on Hi3403
description: Compile GStreamer + Hi3403 plugins and run a pipeline
---
```

`title` is the browser tag and the title on the H1. `description` is the search result and meta tag
subtitle inside.

## Step 3 — Write the text

Refer to the structure of [style guide](style-guide.md):

``` markdown
# Running GStreamer on Hi3403

**Goal**: Compile GStreamer 1.22 + Hi3403 video plugin, and run a pipeline to
output camera data through GStreamer's H.264 encoder.

**Time**: ~1 hour

**Prerequisites**:

- Booted Hi3403 ([quickstart](../get-started/quickstart.md))
- Host has a cross-compilation toolchain

## Step 1 — ...

...
```

## Step 4 — Attach the page to the section

Each section's `index.md` maintains a card grid. New page if it should
Appears on the landing, edit the `index.md` of that section:

``` markdown
<div class="grid cards" markdown>

-   :material-pipe:{ .lg .middle } __GStreamer__

    ---

    Use GStreamer 1.22 with the Hi3403 encoder.

    [:octicons-arrow-right-24: Enter](gstreamer.md)

</div>
```

If your page is the content of a deep sub-section (such as a detail of an ISP),
It doesn’t have to appear on the landing – just being reached directly via a link from an adjacent page will suffice.

## Step 5 — Add image (optional)

Place the image in the `images/` subdirectory of the same directory as the `.md` file:

```
docs/tutorials/
├── gstreamer.md
└── images/
    └── pipeline.png
```

Quote:

``` markdown
![GStreamer pipeline diagram](../community/images/pipeline.svg)
```

Remember to alt text (what’s in square brackets) – Accessibility + SEO.

## Step 6 — Local Preview

``` bash
make serve
```

Browser opens `http://127.0.0.1:8000/` - your new page should
Right there. Try changing a line and saving - the browser will refresh automatically.

## Step 7 — Link Check

Last step before submission:

``` bash
make build && make linkcheck
```

If any internal links are broken, it will be reported. Mention it after repairing it.

## Step 8 — Commit + PR

``` bash
git checkout -b add/gstreamer-tutorial
git add docs/tutorials/gstreamer.md docs/tutorials/index.md docs/tutorials/images/
git commit -m "docs(tutorials): add GStreamer end-to-end tutorial"
git push origin add/gstreamer-tutorial
```

Then click *Pull Request* on Gitee.

## Common mistakes

### "My page does not appear in the sidebar"

Check the filename/path for typos - MkDocs is strictly case-sensitive.

### "Image displays as 404"

The relative path of the link is incorrect. Calculate the path from the perspective of the current page:

``` markdown
<!-- docs/tutorials/gstreamer.md references docs/tutorials/images/pipeline.svg -->
![](../community/images/pipeline.svg)        ✓ correct
![](../community/images/pipeline.svg)      ✓ correct
![](../images/pipeline.svg)       ✗ wrong (site root, not same directory)
```

### "build --strict failed"

Usually an internal link points to a non-existent page. `make linkcheck` can be located.

### "Should there be spaces between Chinese and English?"

add. See the "Chinese and English" section of [style guide](style-guide.md).

## Ready?

Pick a topic you are familiar with, write a page, and submit a PR. The entry gift to the documentation community is writing the first tutorial
Or fix the first typo - all welcome :)