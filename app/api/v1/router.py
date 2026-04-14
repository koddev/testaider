from fastapi import APIRouter
from app.api.v1 import items

router = APIRouter()


@router.get("/ping", tags=["utils"])
async def ping():
    return {"message": "pong"}


router.include_router(items.router)
