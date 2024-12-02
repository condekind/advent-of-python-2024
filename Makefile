

all:
	source .venv/bin/activate && poetry run mypy --check-untyped-defs advent2024/
	source .venv/bin/activate && poetry run ruff check advent2024/
	source .venv/bin/activate && poetry run ruff format advent2024/
	source .venv/bin/activate && poetry run clean
	@rm -rf ./util/__pycache__

.PHONY: fmt lint check

# check is just an alias for lint
check: lint

lint:
	source .venv/bin/activate && poetry run mypy --check-untyped-defs advent2024/
	source .venv/bin/activate && poetry run ruff check advent2024/

fmt:
	source .venv/bin/activate && poetry run ruff format advent2024/

clean:
	source .venv/bin/activate && poetry run clean
	@rm -rf ./util/__pycache__

