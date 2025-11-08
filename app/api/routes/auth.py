from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    # Basic auth implementation
    if request.email == "admin@garlic.com" and request.password == "admin123":
        return LoginResponse(access_token="dummy-token")
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/register")
async def register(request: LoginRequest):
    return {"message": "User registered successfully"}