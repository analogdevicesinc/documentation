SHELL         = /bin/bash
SPHINXOPTS   ?= -j auto
SPHINXBUILD  ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
	@if [ -t 0 ]; then \
		printf "Use \033[0;34madoc serve --sparse <path>\033[0m for faster build time.\n"; \
		read -p "Continue? (yes/no) " yn ; \
		case $$yn in \
			y ) ;; \
			yes ) ;; \
			* ) exit 1 ;; \
		esac ; \
	fi
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
