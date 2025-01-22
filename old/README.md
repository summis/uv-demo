# Project

## Requirements
- `pyenv` Python version manager
- `pyenv-virtualenv` plugin

Add required configuration to your shell setup.
For bash, the configuration is as follows:
```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"
eval "$(pyenv virtualenv-init -)"
```

## Setup

Install required python version
```
pyenv install
```

Create virtual environment
```
pyenv virtualenv .venv
```
Note! The virtual environment is located in `~/.pyenv/versions/`.

Activate virtual environment
```
pyenv activate .venv
```

Install project dependencies
```
pip install -r algorithm/requirements.txt -r algorithm/requirements-dev.txt -r app/requirements.txt -r app/requirements-dev.txt -e algorithm
```

Start application
```
python app/app.py
```

## Common tasks

Run tests
```
pytest
```

Run type-checker
```
mypy .
```

Format code
```
ruff format
```

Lint code
```
ruff check
```

## Project structure
```
.
├── algorithm
│   ├── pyproject.toml
│   ├── requirements-dev.txt
│   ├── requirements.txt
│   ├── src
│   │   └── algorithm
│   │       └── __init__.py
│   └── test
│       └── test_algorithm.py
├── app
│   ├── app.py
│   ├── requirements-dev.txt
│   ├── requirements.txt
│   ├── templates
│   │   └── index.html
│   └── test_app.py
├── mypy.ini
└── README.md
```