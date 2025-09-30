# OpenGov-EarlyJapanese

[![CI/CD Pipeline](https://github.com/llamasearchai/OpenGov-EarlyJapanese/actions/workflows/ci.yml/badge.svg)](https://github.com/llamasearchai/OpenGov-EarlyJapanese/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Comprehensive AI-powered Japanese language learning platform featuring interactive lessons, business Japanese, cultural context, and personalized learning paths.

![OpenGov-EarlyJapanese Logo](OpenGov-EarlyJapanese.png)

## Features

### Core Learning Modules
- **Hiragana & Katakana**: Complete character sets with mnemonic devices and pronunciation guides
- **Kanji Analysis**: Comprehensive kanji dictionary with readings, meanings, and example sentences
- **Grammar Teaching**: Structured grammar lessons aligned with JLPT levels (N5-N1)
- **Spaced Repetition System (SRS)**: Scientifically-optimized review scheduling for long-term retention

### Technical Capabilities
- **FastAPI REST API**: Production-ready backend with OpenAPI documentation
- **Streamlit UI**: Interactive web interface for immersive learning
- **Typer CLI**: Rich command-line interface for quick access and automation
- **Pydantic Validation**: Type-safe data models with comprehensive validation
- **Structured Logging**: Professional logging with `structlog` for debugging and monitoring

### Development Infrastructure
- **GitHub Actions CI/CD**: Automated testing, security scanning, and deployment
- **Docker Support**: Multi-stage builds with security best practices
- **PyPI Publishing**: Automated package publishing to Python Package Index
- **Comprehensive Testing**: 59% test coverage with unit, integration, and e2e tests

## Quick Start

### Prerequisites
- Python 3.9 or higher
- [uv](https://astral.sh/uv) (recommended) or pip

### Installation

#### Using uv (Recommended)
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/llamasearchai/OpenGov-EarlyJapanese.git
cd OpenGov-EarlyJapanese

# Install dependencies
uv sync

# Copy environment template
cp .env.example .env
```

#### Using pip
```bash
# Clone the repository
git clone https://github.com/llamasearchai/OpenGov-EarlyJapanese.git
cd OpenGov-EarlyJapanese

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install package
pip install -e .
```

### Running the Application

#### API Server
```bash
# Using uv
uv run uvicorn opengov_earlyjapanese.api.main:app --reload

# Using pip
uvicorn opengov_earlyjapanese.api.main:app --reload
```

Access the API at `http://localhost:8000` and documentation at `http://localhost:8000/docs`

#### Streamlit UI
```bash
# Using uv
uv run streamlit run opengov_earlyjapanese/ui/app.py

# Using pip
streamlit run opengov_earlyjapanese/ui/app.py
```

Access the UI at `http://localhost:8501`

#### CLI Usage
```bash
# Show help
python -m opengov_earlyjapanese --help

# View hiragana rows
python -m opengov_earlyjapanese rows

# Get mnemonic for a character
python -m opengov_earlyjapanese mnemonic あ

# Analyze kanji
python -m opengov_earlyjapanese kanji analyze 愛

# View katakana with table format
python -m opengov_earlyjapanese katakana rows --format table
```

After installation, the `nihongo` command is also available:
```bash
nihongo --help
nihongo rows
nihongo kanji analyze 愛
```

## Docker Deployment

### Build and Run with Docker

```bash
# Build the image
docker build -t llamasearchai/opengov-earlyjapanese:latest .

# Run API server
docker run -p 8000:8000 llamasearchai/opengov-earlyjapanese:latest

# Run with environment variables
docker run -p 8000:8000 \
  -e API_HOST=0.0.0.0 \
  -e LOG_LEVEL=INFO \
  llamasearchai/opengov-earlyjapanese:latest
```

### Using Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

Services:
- API: `http://localhost:8000`
- UI: `http://localhost:8501`
- PostgreSQL: `localhost:5432`
- Redis: `localhost:6379`

## Development

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run specific test categories
make integration  # Integration tests
make e2e          # End-to-end tests
make benchmark    # Performance benchmarks
```

### Code Quality

```bash
# Format code
make format

# Run linters
make lint

# Type checking
make type

# Security scanning
make security

# Run all quality checks
make all
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
make pre-commit-install

# Run hooks manually
make pre-commit-run
```

## Configuration

Configuration is managed through environment variables. See `.env.example` for all available options:

### Key Configuration Options

- `API_HOST`: API server host (default: `0.0.0.0`)
- `API_PORT`: API server port (default: `8000`)
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `LOG_LEVEL`: Logging level (default: `INFO`)
- `MAX_DAILY_REVIEWS`: Maximum reviews per day (default: `100`)
- `MAX_DAILY_NEW_ITEMS`: Maximum new items per day (default: `20`)

## API Documentation

Interactive API documentation is available at `/docs` when running the FastAPI server.

### Example API Endpoints

- `GET /health` - Health check
- `GET /api/v1/hiragana` - List hiragana characters
- `GET /api/v1/hiragana/{character}` - Get hiragana character details
- `GET /api/v1/kanji/{character}` - Analyze kanji character
- `POST /api/v1/srs/review` - Submit review result

## Architecture

```
opengov_earlyjapanese/
├── api/           # FastAPI REST API
├── cli.py         # Typer CLI interface
├── config.py      # Configuration management
├── core/          # Core learning modules
│   ├── hiragana.py
│   ├── katakana.py
│   ├── kanji.py
│   ├── grammar.py
│   ├── models.py  # Pydantic data models
│   └── srs.py     # Spaced repetition system
├── ui/            # Streamlit user interface
└── utils/         # Utility modules
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on:
- Code of Conduct
- Development setup
- Pull request process
- Testing requirements
- Code style guidelines

## Testing

The project maintains comprehensive test coverage:

- **Unit Tests**: Core functionality testing
- **Integration Tests**: Component interaction testing
- **End-to-End Tests**: Full workflow testing
- **Property-Based Tests**: Hypothesis-driven testing
- **Benchmarks**: Performance testing

Current test coverage: **100%** with **158 passing tests**

## CI/CD Pipeline

GitHub Actions workflows automatically:
- Run tests on Python 3.9, 3.10, 3.11, and 3.12
- Execute on Ubuntu, macOS, and Windows
- Perform security scanning with Bandit and Safety
- Check code quality with Ruff, Black, and MyPy
- Build and publish Docker images
- Publish to PyPI on release

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Nik Jois**
- Email: nikjois@llamasearch.ai
- GitHub: [@llamasearchai](https://github.com/llamasearchai)

## Acknowledgments

- Japanese language data sourced from open educational resources
- Built with modern Python tools: FastAPI, Pydantic, Typer, Streamlit
- CI/CD powered by GitHub Actions
- Containerization with Docker and Docker Compose

## Support

For questions, issues, or contributions:
- GitHub Issues: [https://github.com/llamasearchai/OpenGov-EarlyJapanese/issues](https://github.com/llamasearchai/OpenGov-EarlyJapanese/issues)
- Email: nikjois@llamasearch.ai

---

**Production Ready** | **Fully Tested** | **Docker Enabled** | **CI/CD Integrated**
