###############################################################################
# Common make values.
run      := uv run
sync     := uv sync
python   := $(run) python
blogmore := $(run) blogmore

##############################################################################
# Manage the site.
.PHONY: build
build:				# Build the site
	$(blogmore) build

.PHONY: lint
lint:				# Lint the content and configuration files.
	$(blogmore) lint

.PHONY: serve
serve:				# Locally serve the site for testing.
	$(blogmore) serve --include-drafts

.PHONY: publish
publish:			# Publish the site to GitHub
	$(blogmore) publish

.PHONY: spellcheck
spellcheck:
	bin/spellcheck content/

.PHONY: oldimages
oldimages:			# List dates where I've not updated the images in the attachments folder.
	cd content/extras/attachments && find -E ./ -iregex '.*\.(png|jpg|jpeg)$$' | cut -d'/' -f2,3,4 | sort -u

##############################################################################
# Utility.
.PHONY: setup
setup:				# Set up the environment.
	$(sync)

.PHONY: update
update:				# Update all dependencies
	$(sync) --upgrade

.PHONY: resetup
resetup: realclean		# Recreate the virtual environment from scratch
	make setup

.PHONY: repl
repl:				# Start a Python REPL
	$(python)

.PHONY: realclean
realclean: 		# Clean the venv and build directories
	rm -rf .venv

.PHONY: help
help:				# Display this help
	@grep -Eh "^[a-z]+:.+# " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.+# "}; {printf "%-20s %s\n", $$1, $$2}'

##############################################################################
# Housekeeping tasks.
.PHONY: housekeeping
housekeeping:			# Perform some git housekeeping
	git fsck
	git gc --aggressive
	git remote update --prune

### Makefile ends here
