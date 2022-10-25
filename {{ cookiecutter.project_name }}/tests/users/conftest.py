import pytest
from sqlalchemy.orm import Session

from app.models.users import User


@pytest.fixture(autouse=True)
def create_users(session: Session) -> None:
    users = [
        User(email="alice@gmail.com", password="password"),  # type: ignore[call-arg]
        User(email="robin@gmail.com", password="password"),  # type: ignore[call-arg]
    ]
    session.add_all(users)
    session.commit()
