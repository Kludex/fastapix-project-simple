from typing import Iterable

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

engine = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
SessionLocal = sessionmaker(engine, expire_on_commit=False)


def get_session() -> Iterable[Session]:  # pragma: no cover
    with SessionLocal() as session:
        yield session
