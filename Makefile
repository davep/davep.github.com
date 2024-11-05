###############################################################################
# Common make values.
run     := pipenv run
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
	pipenv sync
	git clone https://github.com/alexandrevicenzi/Flex
	$(themes) -i Flex
	git clone --recursive git@github.com:getpelican/pelican-plugins.git

.PHONY: resetup
resetup:			# Recreate the virtual environment from scratch
	rm -rf $(shell pipenv --venv)
	pipenv sync --dev

.PHONY: depsoutdated
depsoutdated:			# Show a list of outdated dependencies
	pipenv update --outdated

.PHONY: depsupdate
depsupdate:			# Update all dependencies
	pipenv update --dev

.PHONY: depsshow
depsshow:			# Show the dependency graph
	pipenv graph

.PHONY: repl
repl:				# Start a Python REPL
	$(python)

.PHONY: help
help:				# Display this help
	@grep -Eh "^[a-z]+:.+# " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.+# "}; {printf "%-20s %s\n", $$1, $$2}'

### Makefile ends here
