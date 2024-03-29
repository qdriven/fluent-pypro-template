
#* Cleaning
#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove


.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

.PHONY: check-codestyle
check-codestyle:
	poetry run isort --diff --check-only --settings-path pyproject.toml hooks tests
	poetry run black --diff --check --config pyproject.toml hooks tests
	poetry run darglint --verbosity 2 hooks tests

.PHONY: codestyle
codestyle:
	poetry run isort --settings-path pyproject.toml hooks tests
	poetry run black --config pyproject.toml hooks tests

.PHONY: formatting
formatting: codestyle

.PHONY: test
test:
	PYTHONPATH=$(PYTHONPATH) poetry run pytest -c pyproject.toml --cov-report=html --cov=hooks tests/
	mkdir -p assets/images
	poetry run coverage-badge -o assets/images/coverage.svg -f