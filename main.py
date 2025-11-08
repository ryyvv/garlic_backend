from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import garlic, auth, location
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

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(garlic.router, prefix="/api/garlic", tags=["garlic"])
app.include_router(location.router, prefix="/api/location", tags=["location"])

@app.get("/")
async def root():
    return {"message": "Garlic API Hub is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}