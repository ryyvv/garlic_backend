from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os

# user_id != firebase.Uid
class PlantLocationBase(SQLModel):
    region: str
    province: str 
    city: str 
    barangay: str 
    latitude: float
    longitude: float
    user_id: Optional[uuid.UUID] = None

class PlantLocation(PlantLocationBase, table=True):
    __tablename__ = "plant_location"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    region: str = Field(max_length=255) 
    province: str = Field(max_length=255) 
    city: str = Field(max_length=255) 
    barangay: str = Field(max_length=255) 
    latitude: float
    longitude: float
    user_id: Optional[uuid.UUID] = Field(nullable=True)

class PlantLocationCreate(PlantLocationBase):
    pass

class PlantLocationRead(PlantLocationBase):
    id: uuid.UUID

class PlantLocationUpdate(SQLModel):
    region: Optional[str] = None 
    province: Optional[str] = None 
    city: Optional[str] = None 
    barangay: Optional[str] = None 
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    user_id: Optional[uuid.UUID] = None