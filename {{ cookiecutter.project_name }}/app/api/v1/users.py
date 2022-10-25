from typing import Any

from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users() -> Any:
    return [{"name": "Alice"}, {"name": "Bob"}]


@router.get("/{user_id}")
def get_user(user_id: int) -> Any:
    return {"name": "Alice"}


@router.post("/")
def create_user() -> Any:
    return {"name": "Alice"}


@router.put("/{user_id}")
def update_user(user_id: int) -> Any:
    return {"name": "Alice"}
