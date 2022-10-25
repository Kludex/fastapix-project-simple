from typing import Any

from fastapi import FastAPI

from app.api import router as api_router
from app.core.database import engine
from app.models.base import Base


def startup() -> None:  # pragma: no cover
    Base.metadata.drop_all(engine)  # type: ignore[attr-defined]
    Base.metadata.create_all(engine)  # type: ignore[attr-defined]


app = FastAPI(on_startup=[startup])
app.include_router(api_router)


@app.get("/health", include_in_schema=False)
def home() -> Any:
    ...
