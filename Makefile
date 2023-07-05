###############################################################################
# Common make values.
run     := pipenv run
python  := $(run) python
pelican := $(run) pelican
themes  := $(run) pelican-themes

##############################################################################
# Manage the site.
.PHONY: publish
publish:
	$(pelican) --settings publishconf.py

.PHONY: serve
serve:				# Locally serve the site for testing.
	$(pelican) -r -l

.PHONY: themes
themes:			# List the installed themes.
	$(themes) -l

##############################################################################
# Utility.
.PHONY: repl
repl:				# Start a Python REPL
	$(python)

.PHONY: help
help:				# Display this help
	@grep -Eh "^[a-z]+:.+# " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.+# "}; {printf "%-20s %s\n", $$1, $$2}'

### Makefile ends here
