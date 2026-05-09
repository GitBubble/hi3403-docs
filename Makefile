# Pegasus Documentation — top-level build verbs.
#
# Mirrors the Raspberry Pi documentation Makefile vocabulary so that
# anyone familiar with raspberrypi/documentation can navigate this repo
# the same way (`make`, `make clean`, `make serve_html`).
#
# Targets:
#   make            -- build the static site to site/
#   make serve      -- live-preview server on http://127.0.0.1:8000/
#   make serve_html -- alias for `serve` (matches RPi naming)
#   make clean      -- delete site/ and any build cache
#   make migrate    -- run the source-doc migration from ../pegasus
#   make linkcheck  -- offline link check
#   make lint       -- run markdownlint (if installed)
#   make install    -- create .venv and install dependencies
#   make help       -- list targets

.DEFAULT_GOAL := build

VENV        ?= .venv
SYSTEM_PYTHON ?= python3
PYTHON      ?= $(VENV)/bin/python
PIP         ?= $(PYTHON) -m pip
MKDOCS      ?= $(PYTHON) -m mkdocs
PEGASUS_SRC ?= ../pegasus
HI3403_BUILD ?= ../hi3403-build
DEPS_STAMP  := $(VENV)/.deps.stamp

.PHONY: help install build serve serve_html clean migrate linkcheck lint

help:
	@echo "Pegasus Documentation — make targets:"
	@echo "  make install     install Python dependencies"
	@echo "  make build       build the static site to site/"
	@echo "  make serve       live preview at http://127.0.0.1:8000/"
	@echo "  make serve_html  alias for serve"
	@echo "  make migrate     run scripts/migrate.py to ingest pegasus/ docs"
	@echo "  make linkcheck   offline link check"
	@echo "  make lint        markdownlint"
	@echo "  make clean       delete build output"

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
