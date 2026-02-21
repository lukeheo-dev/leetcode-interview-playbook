PYTHON := python3
VENV := .venv
ACTIVATE := source $(VENV)/bin/activate

check-root:
	@test -f pyproject.toml || (echo "❌ Not in repo root (pyproject.toml missing)"; exit 1)

init: check-root
	@echo "==> init env + ruff"
	@if [ -d "$(VENV)" ]; then \
		echo "==> venv exists: $(VENV)"; \
	else \
		$(PYTHON) -m venv $(VENV); \
	fi
	@$(ACTIVATE) && python -m pip install --upgrade pip
	@$(ACTIVATE) && pip install ruff
	@echo "✅ ready"

lint: check-root
	@$(ACTIVATE) && ruff check .

format: check-root
	@$(ACTIVATE) && ruff format .

clean:
	rm -rf $(VENV) __pycache__ */__pycache__

help:
	@echo "make init | make lint | make format | make clean"
