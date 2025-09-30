.PHONY: help install dev-install test test-cov lint format type security clean build pre-commit-install pre-commit-run docs serve streamlit benchmark integration e2e property all

# Default target
help:
	@echo "OpenGov-EarlyJapanese Development Commands"
	@echo "========================================"
	@echo ""
	@echo "Installation & Setup:"
	@echo "  install          Install production dependencies"
	@echo "  dev-install      Install development dependencies"
	@echo "  pre-commit-install Install pre-commit hooks"
	@echo ""
	@echo "Testing & Quality:"
	@echo "  test             Run all tests"
	@echo "  test-cov         Run tests with coverage"
	@echo "  lint             Run linting (ruff, black, isort)"
	@echo "  format           Format code (black, isort)"
	@echo "  type             Run type checking (mypy)"
	@echo "  security         Run security checks (bandit, safety)"
	@echo "  pre-commit-run   Run pre-commit hooks on all files"
	@echo ""
	@echo "Development:"
	@echo "  serve            Run FastAPI server"
	@echo "  streamlit        Run Streamlit UI"
	@echo "  docs             Build documentation"
	@echo "  clean            Clean build artifacts"
	@echo ""

	@echo "Advanced Testing:"
	@echo "  benchmark        Run performance benchmarks"
	@echo "  integration      Run integration tests"
	@echo "  e2e              Run end-to-end tests"
	@echo "  property         Run property-based tests"
	@echo "  all              Run format, lint, type, test"
	@echo ""
	@echo "CI/CD:"
	@echo "  build            Build distribution packages"
	@echo ""

# Installation
install:
	uv sync --frozen

dev-install:
	uv sync --frozen --group dev

pre-commit-install:
	uv run pre-commit install

# Testing & Quality
test:
	uv run pytest -q

test-cov:
	uv run pytest --cov=opengov_earlyjapanese --cov-report=term-missing --cov-report=html

lint:
	uv run ruff check opengov_earlyjapanese tests
	uv run black --check opengov_earlyjapanese tests
	uv run isort --check-only opengov_earlyjapanese tests

format:
	uv run black opengov_earlyjapanese tests
	uv run isort opengov_earlyjapanese tests

type:
	uv run mypy opengov_earlyjapanese

security:
	uv run bandit -r opengov_earlyjapanese -c pyproject.toml
	uv run safety check

pre-commit-run:
	uv run pre-commit run --all-files

# Development
serve:
	uv run uvicorn opengov_earlyjapanese.api.main:app --reload --host 0.0.0.0 --port 8000

streamlit:
	uv run streamlit run opengov_earlyjapanese.ui.app

docs:
	uv run mkdocs build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	rm -f .coverage coverage.xml
	rm -f benchmark.json



# Advanced Testing
benchmark:
	uv run pytest tests/benchmarks/ -m benchmark --benchmark-json=benchmark.json

integration:
	uv run pytest tests/integration/ -m integration -q

e2e:
	uv run pytest tests/e2e/ -m e2e -q

property:
	uv run pytest tests/property/ -m property -q

all:
	$(MAKE) format
	$(MAKE) lint
	$(MAKE) type
	$(MAKE) test

# CI/CD
build:
	uv build
