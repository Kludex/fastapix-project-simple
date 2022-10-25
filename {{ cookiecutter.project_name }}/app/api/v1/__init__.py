from app.api.v1.users import router as users_router
from fastapi import APIRouter

router = APIRouter(prefix="/v1")
router.include_router(users_router)
