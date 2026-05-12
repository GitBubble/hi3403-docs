---
description: How to contribute content to Hi3403 documentation
title: Contribution Guide
---

# Contribution Guide

Contributions to Hi3403 documentation are welcome. The document is maintained by the community, and all changes are made through Gitee Pull Request
Process submission. This guide teaches you how to launch a PR.

## what you can do

- **Fix typos/links** - Just click the *Edit* button directly on Gitee to make changes
- **Complete a small chapter** - For example, a certain API lacks examples
- **Write a new tutorial** - Add a `.md` to the `docs/tutorials/` directory
- **Translate one page zh-CN → en** - add `.en.md` suffix next to the original document
- **Major IA changes or multi-page reconstruction** - open an issue to discuss before taking action

## step

### 1. Fork warehouse

Fork [`HiSpark/pegasus-docs`](https://gitee.com/HiSpark/pegasus-docs) on Gitee
to your own account.

### 2. Clone + create branch

``` bash
git clone https://gitee.com/<your-account>/hi3403-docs.git
cd hi3403-docs
git checkout -b fix/typo-in-quickstart   # descriptive branch name
```

### 3. Install dependencies + start local preview

``` bash
make install        # one-time setup, pip install -r requirements.txt
make serve          # local preview http://127.0.0.1:8000/
```

Open the browser and you can see the complete documentation site.

### 4. Modify the document

Edit the `.md` file under `docs/`. MkDocs will automatically monitor changes and refresh the page.

Please follow [style guide](style-guide.md) when writing.

### 5. Submit

``` bash
git add docs/path/to/your-change.md
git commit -m "docs: fix typo in quickstart step 3"
git push origin fix/typo-in-quickstart
```

### 6. Open a PR

Click *Pull Request* on Gitee and describe clearly:

- What has been changed
- Why change
- Screenshot (if it is a change related to the display effect)

### 7. Waiting for review

The maintainer usually responds within 1 week. possible:

- **Merge directly** - if the changes are small and clear
- **Request a change** - the maintainer will leave a comment and you push the revision
- **Close** – explain why. Major refactorings usually want to be discussed in an issue first

## Write a brand new page

Follow [Add new page](how-to-add-a-page.md) step by step. Short version:

1. Decide which section the page should go to
2. Add the `.md` file in the corresponding directory
3. Add YAML front-matter (`title`, `description`) at the top of the file
4. If the new page should appear in the section's landing card,
Edit the `index.md` of this section to add a card

## translate

The English version is a secondary goal. To translate a page:

1. Found Chinese source file `docs/foo/bar.md`
2. Create `bar.en.md` in the same directory
3. Translate content, retaining all links, images, front-matter
4. Raise a PR

If the corresponding English version does not exist, the i18n plug-in will automatically fallback to the Chinese version, so
There is no "broken" English site - translated pages are in English and untranslated pages are in Chinese.

## Raise an issue

Bugs, feature requests, and suggestions for changing IA are all welcome at
Discussion in [Gitee Issues](https://gitee.com/HiSpark/pegasus-docs/issues).

Please use the following template:

``` markdown
## Description

(One-line description)

## Reproduction / Link

(If it is a bug, provide the page link + screenshot)

## Expected

(What state do you expect?)
```

## code of conduct

- Be friendly to people. Technical disagreements are OK, personal attacks are not.
- Give the reviewer time. Maintainers also contribute part-time.
- Chinese/English are OK, but please keep it consistent throughout a single issue/PR.

## Thanks

Any contribution is important - fix a typo, add a link, translate a paragraph.
The community is the entire reason this document exists.