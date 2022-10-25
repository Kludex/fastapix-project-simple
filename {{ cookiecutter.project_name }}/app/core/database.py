from typing import Iterable

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("sqlite:///", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(engine, expire_on_commit=False, autoflush=False)


def get_session() -> Iterable[Session]:
    with SessionLocal() as session:
        yield session
