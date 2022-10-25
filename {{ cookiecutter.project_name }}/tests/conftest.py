import asyncio
from typing import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.database import get_session
from app.main import app
from app.models.base import Base

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


@pytest.fixture(scope="session", autouse=True)
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    """Reference: https://github.com/pytest-dev/pytest-asyncio/issues/38#issuecomment-264418154"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def create_database() -> None:
    Base.metadata.create_all(engine)  # type: ignore[attr-defined]


@pytest.fixture(scope="session", autouse=True)
def connection() -> Iterator[Connection]:
    with engine.connect() as conn:
        yield conn


@pytest.fixture
def session(connection: Connection) -> Iterator[Session]:
    with connection.begin():
        _session = Session(bind=connection)
        yield _session
        _session.rollback()


@pytest.fixture(autouse=True)
def client(session: Session) -> TestClient:
    app.dependency_overrides[get_session] = lambda: session
    return TestClient(app)
