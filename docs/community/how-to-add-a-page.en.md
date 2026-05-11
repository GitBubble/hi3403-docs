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
| Get started | `docs/get-started/` | quickstart, decision, installation class |
| Boards | `docs/boards/<vendor>/` | Exclusive content for the board |
| OS | `docs/os/<distro>/` | OS porting, dedicated content |
| SoC & Linux | `docs/soc-linux/` | Chip + kernel + startup related |
| Multimedia & AI | `docs/multimedia/` | MPP、ISP、AI |
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
title: 在 Hi3403 上跑 GStreamer
description: 编译 GStreamer + Hi3403 插件，跑一条 pipeline
---
```

`title` is the browser tag and the title on the H1. `description` is the search result and meta tag
subtitle inside.

## Step 3 — Write the text

Refer to the structure of [style guide](style-guide.md):

``` markdown
# 在 Hi3403 上跑 GStreamer

**目标**：编译 GStreamer 1.22 + Hi3403 视频插件，跑一条 pipeline 把
摄像头数据通过 GStreamer 的 H.264 编码器输出。

**用时**：约 1 小时

**前置条件**：

- 启动了 Hi3403（[quickstart](../get-started/quickstart.md)）
- 主机有交叉编译工具链

## 步骤 1 — ...

...
```

## Step 4 — Attach the page to the section

Each section's `index.md` maintains a card grid. New page if it should
Appears on the landing, edit the `index.md` of that section:

``` markdown
<div class="grid cards" markdown>

-   :material-pipe:{ .lg .middle } __GStreamer__

    ---

    用 GStreamer 1.22 接 Hi3403 编码器。

    [:octicons-arrow-right-24: 进入](gstreamer.md)

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
![GStreamer pipeline 示意图](images/pipeline.svg)
```

Remember to alt text (what’s in square brackets) – Accessibility + SEO.

## Step 6 — Local Preview

``` bash
make serve
```

Browser opens <ZXTOKEN0END> - your new page should
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
<!-- docs/tutorials/gstreamer.md 引用 docs/tutorials/images/pipeline.svg -->
![](images/pipeline.svg)        ✓ 对
![](./images/pipeline.svg)      ✓ 对
![](/images/pipeline.svg)       ✗ 错（站根，不是同目录）
```

### "build --strict failed"

Usually an internal link points to a non-existent page. `make linkcheck` can be located.

### "Should there be spaces between Chinese and English?"

add. See the "Chinese and English" section of [style guide](style-guide.md).

## Ready?

Pick a topic you are familiar with, write a page, and submit a PR. The entry gift to the documentation community is writing the first tutorial
Or fix the first typo - all welcome :)