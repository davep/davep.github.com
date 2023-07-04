run     := pipenv run
pelican := $(run) pelican
themes  := $(run) pelican-themes

.PHONY: serve
serve:				# Locally serve the site for testing.
	$(pelican) -r -l

.PHONY: themes
themes:			# List the installed themes.
	$(themes) -l

### Makefile ends here
