# {{ cookiecutter.project_name }}

This is a project generated from [fastapix-project-simple](https://github.com/fastapi-packages/fastapix-project-simple).

## Project Structure

```
{{ cookiecutter.project_name }}/
├── .github/
│   └── workflows/
│       └── main.yml
├── app/
│   ├── __init__.py
|   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── users.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── users.py
│   └── schemas/
│      ├── __init__.py
│      └── users.py
├── tests/
│   ├── __init__.py
|   ├── conftest.py
|   ├── test_main.py
│   └── users/
│       ├── __init__.py
|       ├── conftest.py
│       ├── test_get_users.py
│       ├── test_get_user.py
│       ├── test_create_user.py
│       └── test_update_user.py
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Usage

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
uvicorn app.main:app --reload
```
