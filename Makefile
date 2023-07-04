run     := pipenv run
pelican := $(run) pelican

.PHONY: serve
serve:
	$(pelican) -r -l

### Makefile ends here
