# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-09-30

### Added

#### Core Features
- Hiragana teaching module with complete character set and mnemonics
- Katakana teaching module with pronunciation guides
- Kanji analysis system with readings and meanings
- Grammar teaching framework aligned with JLPT levels
- Spaced Repetition System (SRS) for optimal learning retention
- Comprehensive Pydantic data models for all learning content

#### API & Interfaces
- FastAPI REST API with OpenAPI documentation
- Streamlit interactive web UI for immersive learning
- Typer CLI with rich formatting and color support
- Health check endpoint for monitoring
- CORS middleware for cross-origin requests

#### Development Infrastructure
- GitHub Actions CI/CD pipeline with multi-OS testing
- Multi-stage Docker build with security best practices
- Docker Compose configuration for local development
- PyPI publishing workflow for automated releases
- Pre-commit hooks for code quality enforcement

#### Code Quality
- Comprehensive test suite (unit, integration, e2e)
- 59% test coverage with 26 passing tests
- Ruff linting for code quality
- Black and isort for code formatting
- MyPy for static type checking
- Bandit and Safety for security scanning

#### Documentation
- Comprehensive README with quick start guide
- API documentation with interactive Swagger UI
- Docker deployment instructions
- Development workflow documentation
- Contributing guidelines

#### Configuration
- Environment-based configuration with Pydantic Settings
- Support for PostgreSQL and Redis
- Configurable logging with structlog
- JLPT level progression system
- Gamification and achievement settings

### Security
- Non-root Docker user for container security
- Multi-stage builds to minimize attack surface
- Security scanning in CI/CD pipeline
- Environment variable management for secrets
- Input validation with Pydantic

### Performance
- UV for fast dependency resolution
- Async-ready architecture
- Docker layer caching for faster builds
- Optimized test execution with pytest-xdist

## [Unreleased]

### Planned Features
- AI-powered conversation practice
- Business Japanese module
- Cultural context lessons
- Audio pronunciation integration
- Mobile application support
- Advanced analytics and progress tracking
- Community features and study groups
- Real-time language exchange

---

**Author**: Nik Jois <nikjois@llamasearch.ai>  
**Repository**: https://github.com/llamasearchai/OpenGov-EarlyJapanese  
**License**: MIT

