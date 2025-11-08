from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/config")
async def get_config():
    return {
        "base_url": settings.base_url,
        "environment": settings.environment,
        "api_version": "1.0.0"
    }