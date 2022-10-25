# FastAPI X Project - Simple!

This is part of a series of templates I'm working on.

I'm working on a **composable template system** for FastAPI projects.

## Usage

You'll need to install [`cookiecutter`](https://pypi.org/project/cookiecutter/), and then:

```bash
cookiecutter https://github.com/fastapi-packages/fastapix-project-simple
```

## Project Structure

```
project/
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
│   └── test_users.py
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Supported Generators

This is a note for myself.

- [ ] `Docker Generator`: Create Dockerfile and docker-compose.yml.
- [ ] `Entity Generator`: Create entity e.g. User, Item.
    - This implies creating a model, schemas, and endpoints.
- [ ] `AsyncIO Generator`: Use asyncio instead.
- [ ] `Auth Generator`: Add auth strategies.
- [ ] `TaskQueue Generator`: Add background worker.
    - [ ] Celery
    - [ ] ARQ
    - [ ] Dramatic
    - [ ] Airflow
- [ ] `Database Generator`: Add database.
    - [ ] PostgreSQL
    - [ ] MySQL
    - [ ] SQLite
    - [ ] MongoDB
- [ ] `Migration Setup`: Add migrations setup.
    - [ ] Alembic
- [ ] `Cache Generator`: Add cache.
  - [ ] Redis
  - [ ] Memcached
- [ ] `Deploy Generator` Add deployable strategies.
    - [ ] TBD
- [ ] `Schematesis Generator`: Add schematesis.
- [ ] `DevSetup Generator`: Add development setup.
    - [ ] Tilt
- [ ] `Monorepo Generator`: Add monorepo setup.
  - [ ] Pantsbuild
