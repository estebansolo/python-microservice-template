# Python Microservice Template

This project is a template with best practices for building a python micro-service using Hexagonal Architecture
for a multi domain.

It includes:

* [poetry](https://python-poetry.org/): provides a dependency management and virtual environment setup
* [pydantic](https://pydantic-docs.helpmanual.io/): data validation and modeling 
* [pytest](https://docs.pytest.org/en/7.1.x/): for unit testing
* [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/): measure and show of how much code is executed during testing
* [flake8](https://flake8.pycqa.org/en/latest/): checking the code for stylistic or programming errors
* [isort](https://pycqa.github.io/isort/): sort imports alphabetically and automatically separate them into sections.
* [unimport](https://unimport.hakancelik.dev/): Removes unused imports

## Usage

Running unit test

```bash
poetry run pytest
```

Check and apply sort over all project imports

```bash
poetry run isort .
poetry run isort . --check-only
poetry run isort . --diff
```

Check and remove unused imports

```bash
poetry run unimport -c setup.cfg
poetry run unimport -c setup.cfg --remove
```

Code coverage report

```bash
poetry run pytest --cov="."
poetry run pytest --cov="." --cov-report html
```

Code checking

```bash
poetry run flake8 .
```
