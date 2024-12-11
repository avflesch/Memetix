# Development Guide

## Project Setup

1. Clone the repository:
```bash
git clone https://github.com/memesphere/memesphere.git
cd memesphere
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Code Style

We follow these conventions:
- PEP 8 for Python code style
- Google style docstrings
- Type hints for all functions
- Maximum line length of 88 characters

Use pre-commit hooks:
```bash
pre-commit install
```

## Testing

Run tests:
```bash
pytest tests/
```

With coverage:
```bash
pytest --cov=memesphere tests/
```

## Adding New Features

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Implement your feature:
   - Add tests in `tests/`
   - Update documentation
   - Add type hints
   - Follow code style guidelines

3. Submit a pull request:
   - Clear description
   - Reference any related issues
   - Include test results

## Documentation

Generate documentation:
```bash
cd docs
make html
```

## Release Process

1. Update version in `setup.py`
2. Update CHANGELOG.md
3. Create release branch
4. Submit PR for review
5. Tag release after merge 