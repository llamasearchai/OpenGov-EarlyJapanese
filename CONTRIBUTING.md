# Contributing to OpenGov-EarlyJapanese

Thank you for your interest in contributing to OpenGov-EarlyJapanese! We welcome contributions from everyone, regardless of experience level.

## Quick Start for Contributors

### 1. Set Up Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/your-username/earlyjapanese.git
cd opengov-earlyjapanese

# Install uv (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --group dev

# Install pre-commit hooks
uv run pre-commit install

# Set up environment
cp .env.example .env
# Edit .env with your development settings
```

### 2. Run Quality Checks

```bash
# Format code
make format

# Run linting
make lint

# Run type checking
make type

# Run tests
make test

# Run all checks
make all
```

### 3. Make Your Changes

- Create a feature branch: `git checkout -b feature/amazing-feature`
- Make your changes following our coding standards
- Add tests for new functionality
- Update documentation as needed
- Run quality checks: `make all`

### 4. Submit Your Contribution

```bash
# Commit your changes
git add .
git commit -m "Add amazing feature"

# Push to your fork
git push origin feature/amazing-feature

# Create a Pull Request
# Go to GitHub and create a PR from your feature branch
```

## Contribution Guidelines

### Code Standards

#### Python Style
- Follow [PEP 8](https://pep8.org/) guidelines
- Use `black` for code formatting (configured in `pyproject.toml`)
- Use `isort` for import sorting
- Use `ruff` for linting (replaces flake8, pylint, etc.)
- Use `mypy` for type checking

#### Documentation
- Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Update README.md for user-facing changes
- Update API documentation for new endpoints
- Add examples for new features

#### Testing
- Write unit tests for all new functionality
- Add integration tests for external service interactions
- Include property-based tests where appropriate
- Maintain >90% test coverage
- Use descriptive test names

### Commit Conventions

We follow [Conventional Commits](https://conventionalcommits.org/) format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(tui): add hiragana practice mode
fix(api): resolve kanji lookup timeout
docs: update installation instructions
test: add property-based tests for grammar
```

### Pull Request Process

1. **Create a Feature Branch**: `git checkout -b feature/your-feature-name`
2. **Make Your Changes**: Implement your feature or fix
3. **Add Tests**: Ensure all tests pass
4. **Update Documentation**: Update relevant docs
5. **Run Quality Checks**: `make all`
6. **Submit PR**: Create a pull request with a clear description

#### PR Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Type hints added/updated
- [ ] Security considerations addressed
```

## Testing Guidelines

### Unit Tests
- Test individual functions and methods
- Mock external dependencies
- Use descriptive test names
- Follow Arrange-Act-Assert pattern

```python
def test_hiragana_lesson_creation():
    """Test that hiragana lessons are created correctly."""
    teacher = HiraganaTeacher()

    lesson = teacher.get_lesson("a_row")

    assert lesson.row == "a_row"
    assert len(lesson.characters) == 5
    assert all(char in teacher.characters for char in lesson.characters)
```

### Integration Tests
- Test interactions between components
- Use test databases and mock services where possible

```python
@pytest.mark.integration
def test_api_health(client):
    # Example: test FastAPI health endpoint with a test client
    from fastapi.testclient import TestClient
    from opengov_earlyjapanese.api.main import app

    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json().get("status") == "ok"
```

### Property-Based Tests
- Use `hypothesis` for property-based testing
- Test with generated data
- Find edge cases automatically

```python
@given(st.text(min_size=1, max_size=10))
def test_kanji_analysis_with_various_inputs(character):
    """Test kanji analysis with various character inputs."""
    master = KanjiMaster()

    # Should not raise exceptions
    result = master.analyze(character)

    # If character exists, should return valid analysis
    if result:
        assert result.character == character
        assert isinstance(result.meanings, list)
```

## Documentation Guidelines

### Code Documentation
- Add docstrings to all public functions, classes, and methods
- Use descriptive parameter and return value documentation
- Include usage examples where helpful

```python
def analyze_kanji(self, character: str) -> Optional[KanjiAnalysis]:
    """
    Analyze a kanji character and return detailed information.

    Args:
        character: The kanji character to analyze (e.g., "愛")

    Returns:
        KanjiAnalysis object with meanings, readings, and mnemonics,
        or None if character is not found

    Example:
        >>> master = KanjiMaster()
        >>> analysis = master.analyze("愛")
        >>> print(analysis.meanings)
        ['love', 'affection']
    """
```

### User Documentation
- Update README.md for user-facing changes
- Add examples and use cases
- Include troubleshooting information
- Keep instructions clear and up-to-date

### API Documentation
- Document all API endpoints
- Include request/response examples
- Specify authentication requirements
- Note rate limits and error codes

## Security Considerations

When contributing code, please consider:

- **Input Validation**: Validate all user inputs
- **SQL Injection**: Use parameterized queries
- **XSS Prevention**: Escape user-generated content
- **Authentication**: Implement proper auth checks
- **Authorization**: Verify user permissions
- **Secrets Management**: Never commit secrets
- **Dependency Security**: Keep dependencies updated

## Reporting Issues

### Bug Reports
- Use the GitHub issue tracker
- Include clear reproduction steps
- Provide expected vs actual behavior
- Include error messages and stack traces
- Specify environment details (OS, Python version, etc.)

### Feature Requests
- Describe the problem you're trying to solve
- Explain why existing features don't suffice
- Provide concrete examples of desired usage
- Consider edge cases and error conditions

## Architecture Guidelines

### Code Organization
- Follow the established package structure
- Keep modules focused and single-purpose
- Use dependency injection for testability
- Follow SOLID principles

### Performance Considerations
- Profile code for performance bottlenecks
- Use appropriate data structures
- Implement caching where beneficial
- Consider memory usage for large datasets

### Error Handling
- Use appropriate exception types
- Provide meaningful error messages
- Log errors with context
- Handle edge cases gracefully

## Getting Help

### Resources
- **Documentation**: Check the docs/ directory
- **Issues**: Search existing GitHub issues
- **Discussions**: Use GitHub Discussions for questions
- **Code Review**: Learn from existing PRs

### Community
- **Discord**: Join our community Discord (link in README)
- **Forum**: Participate in discussions
- **Office Hours**: Join weekly office hours for help

## Recognition

Contributors are recognized through:
- **GitHub Contributors** page
- **Release Notes** mentioning major contributions
- **Community Spotlight** in our newsletter
- **Special Badges** for significant contributions

---

Thank you for contributing to OpenGov-EarlyJapanese! Your help makes Japanese language learning more accessible to everyone.
