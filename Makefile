.PHONY: all lint type test test-cov

CMD:=poetry run
PYMODULE:=damm32

all: lint type test

lint:
	$(CMD) flake8 $(PYMODULE) tests

type:
	$(CMD) mypy $(PYMODULE)

test:
	$(CMD) pytest --cov=$(PYMODULE) tests

test-cov:
	$(CMD) pytest --cov=$(PYMODULE) tests --cov-report html
