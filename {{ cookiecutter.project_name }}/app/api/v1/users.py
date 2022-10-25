from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models.users import User
from app.schemas.users import UserCreate, UserOutput, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserOutput])
def get_users(session: Session = Depends(get_session)) -> Any:
    users = session.execute(select(User)).scalars().all()
    return users


@router.get("/{user_id}", response_model=UserOutput)
def get_user(user_id: int, session: Session = Depends(get_session)) -> Any:
    user = session.execute(select(User).filter(User.id == user_id)).scalars().first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/", response_model=UserOutput)
def create_user(input: UserCreate, session: Session = Depends(get_session)) -> Any:
    try:
        user = User(email=input.email, password=input.password)  # type: ignore[call-arg]
        session.add(user)
        session.commit()
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists.")

    return user


@router.put("/{user_id}", response_model=UserOutput)
def update_user(
    user_id: int, input: UserUpdate, session: Session = Depends(get_session)
) -> Any:
    user = session.execute(select(User).filter(User.id == user_id)).scalars().first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")

    try:
        for key, value in input.dict(exclude_unset=True).items():
            setattr(user, key, value)
        session.commit()
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists.")
    return user
