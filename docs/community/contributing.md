---
title: 贡献指南
description: 如何为 Hi3403 文档贡献内容
---

# 贡献指南

欢迎为 Hi3403 文档贡献。文档由社区维护，所有改动通过 Gitee Pull Request
流程提交。本指南教你怎么发起一次 PR。

## 你能做的

- **修笔误 / 链接** —— 直接在 Gitee 上点 *编辑* 按钮就能改
- **补一个小章节** —— 比如某个 API 缺少示例
- **写一篇新教程** —— 在 `docs/tutorials/` 目录下加一个 `.md`
- **翻译一页 zh-CN → en** —— 在原文件旁加 `.en.md` 后缀
- **大改 IA 或多页重构** —— 先开 issue 讨论再动手

## 步骤

### 1. Fork 仓库

在 Gitee 上 fork [`HiSpark/pegasus-docs`](https://gitee.com/HiSpark/pegasus-docs)
到你自己的账户。

### 2. 克隆 + 创建分支

``` bash
git clone https://gitee.com/<你的账号>/hi3403-docs.git
cd hi3403-docs
git checkout -b fix/typo-in-quickstart   # 描述性的分支名
```

### 3. 安装依赖 + 启动本地预览

``` bash
make install        # 一次性，pip install -r requirements.txt
make serve          # 本地预览 http://127.0.0.1:8000/
```

打开浏览器，能看到完整的文档站。

### 4. 改文档

编辑 `docs/` 下的 `.md` 文件。MkDocs 会自动监听变化、刷新页面。

写作请遵守 [风格指南](style-guide.md)。

### 5. 提交

``` bash
git add docs/path/to/your-change.md
git commit -m "docs: fix typo in quickstart 步骤 3"
git push origin fix/typo-in-quickstart
```

### 6. 开 PR

在 Gitee 上点 *Pull Request*，描述清楚：

- 改了什么
- 为什么改
- 截图（如果是显示效果相关的改动）

### 7. 等审查

维护者通常会在 1 周内回复。可能：

- **直接合并** —— 如果改动小且清晰
- **要求修改** —— 维护者会留评论，你 push 修订
- **关闭** —— 解释原因。重大重构通常希望先在 issue 讨论

## 写一篇全新的页面

跟着 [添加新页面](how-to-add-a-page.md) 一步步走。简短版：

1. 决定页面去哪个 section
2. 在对应目录下加 `.md` 文件
3. 在文件顶部加 YAML front-matter（`title`、`description`）
4. 如果新页面应该出现在该 section 的 landing 卡片里，
   编辑该 section 的 `index.md` 加一张卡

## 翻译

英文版本是次级目标。要翻译一页：

1. 找到中文源文件 `docs/foo/bar.md`
2. 在同一目录下创建 `bar.en.md`
3. 翻译内容，保留所有的链接、图片、front-matter
4. 提 PR

如果对应的英文版不存在，i18n 插件会自动 fallback 到中文版，所以
不存在 "残缺" 的英文站点 —— 已翻译的页面是英文，未翻译的是中文。

## 提 issue

bug、功能请求、改 IA 的提议都欢迎在
[Gitee Issues](https://gitee.com/HiSpark/pegasus-docs/issues) 里讨论。

请用以下模板：

``` markdown
## 描述

（一句话描述）

## 重现 / 链接

（如果是 bug，给出页面链接 + 截图）

## 期望

（你希望的状态是什么）
```

## 行为准则

- 对人友好。技术分歧 OK，人身攻击不 OK。
- 给 reviewer 时间。维护者也是兼职贡献。
- 中文 / 英文都 OK，但请**保持一种**贯穿单条 issue / PR。

## 谢谢

任何贡献都很重要 —— 修一个错别字、补一行链接、翻译一段话。
社区是这套文档存在的全部理由。
