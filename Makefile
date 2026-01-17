###############################################################################
# Common make values.
run     := uv run
sync    := uv sync
python  := $(run) python
pelican := $(run) pelican
themes  := $(run) pelican-themes

##############################################################################
# Manage the site.
.PHONY: generate
generate:
	$(pelican) --settings publishconf.py

.PHONY: serve
serve:				# Locally serve the site for testing.
	$(pelican) -r -l

.PHONY: themes
themes:			# List the installed themes.
	$(themes) -l

##############################################################################
# Utility.
.PHONY: setup
setup:				# Set up the environment.
	$(sync)
	git clone https://github.com/alexandrevicenzi/Flex
	$(themes) -i Flex
	git clone --recursive git@github.com:getpelican/pelican-plugins.git

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
	rm -rf Flex
	rm -rf pelican-plugins

.PHONY: help
help:				# Display this help
	@grep -Eh "^[a-z]+:.+# " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.+# "}; {printf "%-20s %s\n", $$1, $$2}'

### Makefile ends here
