# Project

## Requirements
- `uv` Python project manager

## Setup

Start application
```
uv run --package app app/app.py
```

## Common tasks

Run tests separately for each project
```
uv sync --exact --package app && uv run --group test pytest app
uv sync --exact --package algorithm && uv run --group test pytest algorithm
```

Run type-checker
```
uv sync --all-packages && uv run --group type-check mypy .
```

Format code
```
uvx ruff format
```

Lint code
```
uvx ruff check
```

## Project structure
```
.
├── algorithm
│   ├── pyproject.toml
│   ├── src
│   │   └── algorithm
│   │       └── __init__.py
│   └── test
│       └── test_algorithm.py
├── app
│   ├── app.py
│   ├── pyproject.toml
│   ├── templates
│   │   └── index.html
│   └── test_app.py
├── mypy.ini
├── pyproject.toml
├── README.md
└── uv.lock
```