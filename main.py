from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import (
    auth, garlic_variety, garlic_variety_category_bullet_details,
    garlic_variety_sub_bullet_details, garlic_variety_images,
    plant_location, garlic_plant, users, garlic_images_list, base, location
)
from app.core.config import settings

app = FastAPI(
    title="Garlic API Hub",
    description="API for Garlic Plant Management System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(garlic_variety.router, prefix="/api/v1/garlic-variety", tags=["garlic-variety"])
app.include_router(garlic_variety_category_bullet_details.router, prefix="/api/v1/variety-category-bullets", tags=["variety-category-bullets"])
app.include_router(garlic_variety_sub_bullet_details.router, prefix="/api/v1/variety-sub-bullets", tags=["variety-sub-bullets"])
app.include_router(garlic_variety_images.router, prefix="/api/v1/variety-images", tags=["variety-images"])
app.include_router(plant_location.router, prefix="/api/v1/plant-location", tags=["plant-location"])
app.include_router(garlic_plant.router, prefix="/api/v1/garlic-plant", tags=["garlic-plant"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(garlic_images_list.router, prefix="/api/v1/garlic-images", tags=["garlic-images"])
app.include_router(location.router, prefix="/api/v1/location", tags=["location"])

app.include_router(base.router, prefix="/api/v1", tags=["base"])

@app.get("/")
async def root():
    return {
        "message": "Garlic API Hub is running",
        "base_url": settings.base_url,
        "environment": settings.environment,
        "docs_url": f"{settings.base_url}/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "base_url": settings.base_url}