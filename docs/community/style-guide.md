---
title: 风格指南
description: Pegasus 文档的写作约定
---

# 风格指南

这是写 Pegasus 文档时的约定。目标：所有页面读起来风格一致、专业、
对新读者友好。

## 语气

- **直接、平视**。不要 "我们" / "我" / "您" / "敬请"。
- **客观**。"性能更好" 要给数据；"推荐" 要给理由。
- **不卖关子**。把结论放第一段。

| 不要 | 要 |
|---|---|
| "亲爱的开发者，欢迎使用 SVP！" | "SVP 是 Hi3403 的 NPU。本节介绍它的开发模型。" |
| "您可以根据需要修改" | "可以修改" |
| "为了更好的体验，建议您..." | "建议..." |

## 结构

每页的标准结构：

```
---
title: 短标题
description: 一句话描述（搜索结果里会显示）
---

# 标题

一段话引言：这页讲什么、读完能做什么。

## 二级标题

正文。

## 二级标题

正文。

## 接下来

跳转到下一步的卡片网格。
```

页面长度尽量在 **5–10 屏**。超长的拆成多页。

## 标题层级

- `#` —— 只在文件首部出现一次（页面标题）
- `##` —— 主要段落
- `###` —— 子段落
- `####` —— 极少用

不要跳级（`#` 直接跳到 `###`）。

## 链接

**用相对路径**链接到本站其他页面：

```markdown
[ISP 调优](../multimedia/isp/tuning/index.md)    ✓ 对
[ISP 调优](https://docs.example.com/multimedia/...)  ✗ 错
```

外部链接保留 https。**不要**给 https 链接加 "(opens in new tab)" 之类的
说明 —— 浏览器自己会处理。

## 代码块

总是给语言标签：

````markdown
``` bash
make build
```
````

不要写裸 ``` ```。

命令行示例**不带提示符**（`$` `#`）—— 复制粘贴更方便：

| 不要 | 要 |
|---|---|
| `$ make build` | `make build` |
| `# apt update` | `sudo apt update` |

需要区分用户/root 时显式写 `sudo`。

## 命令输出

把期望输出放在另一个代码块里，不要混在命令里：

````markdown
``` bash
make verify
```

期望输出：

```
✓ All 5 downloads verified
```
````

## Admonition 块

用 Material 主题提供的 admonition：

```markdown
!!! note "标题（可选）"

    这是一条 note。

!!! warning

    这是一条 warning。
```

可用类型：`note`、`tip`、`info`、`warning`、`danger`、`example`、
`question`、`bug`。

## 卡片网格

每个 section landing 用 grid cards：

```markdown
<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } __标题__

    ---

    一句话描述。

    [:octicons-arrow-right-24: 进入](path/to/page.md)

</div>
```

图标用 [Material Icons](https://pictogrammers.github.io/@mdi/font/2.0.46/) 或
Octicons / Simple Icons。一个 section 内尽量统一图标家族。

## 表格

用 pipe 表格，不用 HTML：

```markdown
| 列 1 | 列 2 |
|---|---|
| 值 1 | 值 2 |
```

复杂表格如果 markdown 撑不住，改成 admonition + 多个表格。

## 图片

放在每页的同名子目录里：

```
docs/
└── multimedia/
    └── isp/
        ├── tuning.md
        └── images/
            └── awb-flow.png
```

引用：`![AWB 收敛流程](images/awb-flow.png)`

加 `alt` 文本（无障碍访问 + SEO）。

## 中英文

- **中英混排时加空格**：`使用 ATC 工具`，不是 `使用ATC工具`
- **数字、单位、英文标点**：用半角，前后加空格 —— `8 GB`、`30 fps`、`5.5 V`
- **中文里用中文标点**：`，。：；！？` —— 不要 `,.;!?`
- 引用代码、文件名、变量时用反引号：\`isp_awb.cfg\`

## 缩写

第一次出现时加全称：

```
ISP（Image Signal Processor，图像信号处理器）负责...
```

之后可以只用缩写。每页的"接下来"或"参考"段落不需要重复全称。

[术语表](../reference/glossary.md) 里有所有缩写的统一定义 —— 写新缩写时
先查表，避免分歧。

## 不要

- ❌ Emoji 满天飞 —— 标题里偶尔用 ✓ ✗ 提醒效果还行；正文里慎用
- ❌ "更高效" / "更快" 而不给基线
- ❌ 长段落里夹大量代码 —— 拆成短段 + 代码块
- ❌ 翻译腔（"As you can see..." → "如你所见..."）

## 校对清单

提 PR 前过一遍：

- [ ] 标题层级是否合理（不跳级）
- [ ] 内部链接都用相对路径
- [ ] 代码块都有语言标签
- [ ] 中英之间有空格
- [ ] 缩写第一次出现时给了全称
- [ ] 跑了 `make serve` 本地看过效果
- [ ] （理想情况）跑了 `make linkcheck` 没断链
