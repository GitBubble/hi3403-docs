---
title: 添加一个新页面
description: 一份手把手指南：克隆 → 写一页 → 本地预览 → 提 PR
---

# 添加一个新页面

本文是给第一次给 Hi3403 文档加页面的贡献者的逐步教程。
跟着做大概 15 分钟。

## 决定页面去哪

每个页面对应 IA 里的一个具体位置。下面是 7 个 section 对应的目录：

| Section | 目录 | 装什么 |
|---|---|---|
| 快速开始 | `docs/get-started/` | quickstart、决策、安装类 |
| 开发板 | `docs/boards/<vendor>/` | 板子专属内容 |
| 操作系统 | `docs/os/<distro>/` | OS 移植、专用内容 |
| SoC 与 Linux | `docs/soc-linux/` | 芯片 + 内核 + 启动相关 |
| 多媒体与 AI | `docs/multimedia/` | MPP、ISP、AI |
| 工具 | `docs/tools/` | 工具类 |
| 参考 | `docs/reference/` | API、FAQ、配置 |
| 教程 | `docs/tutorials/` | 端到端实战 |
| 社区 | `docs/community/` | 流程类 |

**例子**：你写了一篇 "在 Hi3403 上跑 GStreamer" 的教程。这是端到端实战，
所以放 `docs/tutorials/gstreamer.md`。

## 步骤 1 — 创建文件

``` bash
cd hi3403-docs
$EDITOR docs/tutorials/gstreamer.md
```

## 步骤 2 — 加 front-matter

每个页面顶部都需要 YAML front-matter：

``` markdown
---
title: 在 Hi3403 上跑 GStreamer
description: 编译 GStreamer + Hi3403 插件，跑一条 pipeline
---
```

`title` 是浏览器标签和 H1 上的标题。`description` 是搜索结果和 meta 标签
里的副标题。

## 步骤 3 — 写正文

参考 [风格指南](style-guide.md) 的结构：

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

## 步骤 4 — 把页面接到 section 里

每个 section 的 `index.md` 维护一个卡片网格（card grid）。新页面如果应该
出现在 landing 上，编辑该 section 的 `index.md`：

``` markdown
<div class="grid cards" markdown>

-   :material-pipe:{ .lg .middle } __GStreamer__

    ---

    用 GStreamer 1.22 接 Hi3403 编码器。

    [:octicons-arrow-right-24: 进入](gstreamer.md)

</div>
```

如果你的页面是某个深层 sub-section 的内容（比如 ISP 的某个细节），
不一定要出现在 landing 上 —— 直接通过相邻页面的链接到达就够。

## 步骤 5 — 加图（可选）

把图片放在跟 `.md` 文件同目录的 `images/` 子目录里：

```
docs/tutorials/
├── gstreamer.md
└── images/
    └── pipeline.png
```

引用：

``` markdown
![GStreamer pipeline 示意图](images/pipeline.png)
```

记得给 alt 文本（方括号里的内容）—— 无障碍 + SEO。

## 步骤 6 — 本地预览

``` bash
make serve
```

浏览器打开 `http://127.0.0.1:8000/tutorials/gstreamer/` —— 你的新页面应该
就在那（`make serve` 会启动 MkDocs 开发服务器在 8000 端口）。试试改一行、
保存 —— 浏览器会自动刷新。

## 步骤 7 — 链接检查

提交前最后一步：

``` bash
make build && make linkcheck
```

如果有内部链接断了会报出来。修完再提。

## 步骤 8 — 提交 + PR

``` bash
git checkout -b add/gstreamer-tutorial
git add docs/tutorials/gstreamer.md docs/tutorials/index.md docs/tutorials/images/
git commit -m "docs(tutorials): add GStreamer end-to-end tutorial"
git push origin add/gstreamer-tutorial
```

然后在 Gitee 上点 *Pull Request*。

## 常见错误

### "我的页面在侧边栏不显示"

检查文件名 / 路径有没有错字 —— MkDocs 严格区分大小写。

### "图片显示成 404"

链接的相对路径写错。从当前页面的角度算路径：

``` markdown
<!-- docs/tutorials/gstreamer.md 引用 docs/tutorials/images/pipeline.png -->
![](images/pipeline.png)        ✓ 对
![](./images/pipeline.png)      ✓ 对
![](/images/pipeline.png)       ✗ 错（站根，不是同目录）
```

### "build --strict 失败"

通常是某个内部链接指向不存在的页面。`make linkcheck` 能定位。

### "中英文之间该不该加空格"

加。看 [风格指南](style-guide.md) 的 "中英文" 一节。

## 准备好了？

挑一个你熟悉的主题，写一页，提 PR。文档社区的入门礼是写第一篇教程
或修第一个错别字 —— 都欢迎 :)
