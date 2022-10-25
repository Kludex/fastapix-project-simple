# FastAPI X Project - Simple!

This is part of a series of templates I'm working on.

I'm working on a **composable template system** for FastAPI projects.

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
├── .pyproject.toml
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Supported Generators

This is a note for myself.

- [ ] `Entity Generator`: Create entity e.g. User, Item.
    - This implies creating a model, schemas, and endpoints.
- [ ] `Auth Generator`: Add auth strategies.
- [ ] `TaskQueue Generator`: Add background worker e.g. Celery, ARQ, Dramatiq etc.
- [ ] `Database Generator`: Add database e.g. PostgreSQL, MySQL, SQLite.
    - This should also include NoSQL databases.
- [ ] `Cache Generator`: Add cache e.g. Redis, Memcached.
- [ ] `Deploy Generator` Add deployable strategies.
- [ ] `Schematesis Generator`: Add schematesis.
- [ ] `DevSetup Generator`: Add development setup e.g. Tilt.
- [ ] `Monorepo Generator`: Add monorepo setup e.g. Pantsbuild.
