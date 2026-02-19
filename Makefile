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

.PHONY: serve
serve:				# Locally serve the site for testing.
	$(blogmore) serve

.PHONY: publish
publish:			# Publish the site to GitHub
	$(blogmore) publish

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

### Makefile ends here
