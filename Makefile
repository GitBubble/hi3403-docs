# Pegasus Documentation — top-level build verbs.
#
# Mirrors the Raspberry Pi documentation Makefile vocabulary so that
# anyone familiar with raspberrypi/documentation can navigate this repo
# the same way (`make`, `make clean`, `make serve_html`).
#
# Targets:
#   make             -- build the static site to site/
#   make serve       -- live-preview server on http://127.0.0.1:8000/
#   make serve_html  -- alias for `serve` (matches RPi naming)
#   make clean       -- delete site/ and any build cache
#   make migrate     -- run the source-doc migration from ../pegasus
#   make linkcheck   -- offline link check
#   make lint        -- run markdownlint (if installed)
#   make install     -- create .venv and install dependencies
#   make translate   -- generate missing .en.md siblings (needs network)
#   make i18n-status -- print zh:en coverage by section
#   make help        -- list targets

.DEFAULT_GOAL := build

VENV        ?= .venv
SYSTEM_PYTHON ?= python3
PYTHON      ?= $(VENV)/bin/python
PIP         ?= $(PYTHON) -m pip
MKDOCS      ?= $(PYTHON) -m mkdocs
PEGASUS_SRC ?= ../pegasus
HI3403_BUILD ?= ../hi3403-build
DEPS_STAMP  := $(VENV)/.deps.stamp

.PHONY: help install build serve serve_html clean migrate linkcheck lint translate translate-patch i18n-status

help:
	@echo "Pegasus Documentation — make targets:"
	@echo "  make install      install Python dependencies"
	@echo "  make build        build the static site to site/"
	@echo "  make serve        live preview at http://127.0.0.1:8000/"
	@echo "  make reserve      rebuild + restart dev server (fresh CSS/JS)"
	@echo "  make serve_html   alias for serve"
	@echo "  make migrate      run scripts/migrate.py to ingest pegasus/ docs"
	@echo "  make translate      generate missing .en.md siblings
		@echo "  make translate-patch  translate remaining Chinese in .en.md files""
	@echo "  make i18n-status  print zh:en coverage"
	@echo "  make linkcheck    offline link check"
	@echo "  make lint         markdownlint"
	@echo "  make clean        delete build output"

$(PYTHON):
	$(SYSTEM_PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip

$(DEPS_STAMP): requirements.txt | $(PYTHON)
	$(PIP) install -r requirements.txt
	@touch $@

install: $(DEPS_STAMP)

build: $(DEPS_STAMP)
	$(MKDOCS) build --strict

serve serve_html: $(DEPS_STAMP)
	$(MKDOCS) serve

reserve: $(DEPS_STAMP)
	$(MKDOCS) build
	pkill -f "mkdocs serve" 2>/dev/null; sleep 1
	$(MKDOCS) serve

clean:
	rm -rf site/ .cache/

migrate:
	$(PYTHON) scripts/migrate.py \
		--pegasus "$(PEGASUS_SRC)" \
		--hi3403-build "$(HI3403_BUILD)" \
		--out docs/

linkcheck:
	@if [ ! -d site ]; then $(MAKE) build; fi
	$(PYTHON) scripts/linkcheck.py site/

lint:
	@command -v markdownlint >/dev/null 2>&1 || { \
		echo "markdownlint not installed; skip"; exit 0; }
	markdownlint 'docs/**/*.md'

translate: $(DEPS_STAMP)
	@$(PIP) install -q deep-translator python-frontmatter 2>/dev/null || true
	$(PYTHON) scripts/translate_docs.py

translate-patch: $(DEPS_STAMP)
	@$(PIP) install -q deep-translator python-frontmatter 2>/dev/null || true
	$(PYTHON) scripts/translate_deepl.py

i18n-status:
	@total=$$(find docs -name '*.md' -not -name '*.en.md' | wc -l); \
	translated=$$(find docs -name '*.md' -not -name '*.en.md' | while read -r f; do \
	  [ -f "$${f%.md}.en.md" ] && echo "$$f"; \
	done | wc -l); \
	pct=$$(awk "BEGIN {printf \"%.1f\", $$translated/$$total*100}"); \
	printf "Coverage: %d / %d zh pages have an .en.md sibling (%.1f%%)\n" \
	  "$$translated" "$$total" "$$pct"; \
	echo "Untranslated by section:"; \
	for d in docs/get-started docs/boards docs/os docs/soc-linux docs/multimedia docs/tools docs/reference docs/community docs/tutorials; do \
	  name=$${d#docs/}; \
	  untrans=$$(find "$$d" -name '*.md' -not -name '*.en.md' 2>/dev/null | while read -r f; do \
	    [ -f "$${f%.md}.en.md" ] || echo "$$f"; \
	  done | wc -l); \
	  total_d=$$(find "$$d" -name '*.md' -not -name '*.en.md' 2>/dev/null | wc -l); \
	  printf "  %-15s %3d / %3d untranslated\n" "$$name" "$$untrans" "$$total_d"; \
	done
