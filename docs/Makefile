# Minimal makefile for Sphinx docs

SPHINXOPTS =
SPHINXBUILD = python -msphinx
SPHINXPROJ = privates
SOURCEDIR = source
BUILDDIR = build

help:
    @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
    @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
