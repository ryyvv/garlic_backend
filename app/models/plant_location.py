from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os

class PlantLocationBase(SQLModel):
    reg_name: str
    reg_code: str
    prov_name: str
    prov_code: str
    mun_name: str
    mun_code: str
    brgy_name: str
    brgy_code: str
    lat: float
    long: float

class PlantLocation(PlantLocationBase, table=True):
    __tablename__ = "plant_location"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    reg_name: str = Field(max_length=255)
    reg_code: str = Field(max_length=255)
    prov_name: str = Field(max_length=255)
    prov_code: str = Field(max_length=255)
    mun_name: str = Field(max_length=255)
    mun_code: str = Field(max_length=255)
    brgy_name: str = Field(max_length=255)
    brgy_code: str = Field(max_length=255)
    lat: float
    long: float

class PlantLocationCreate(PlantLocationBase):
    pass

class PlantLocationRead(PlantLocationBase):
    id: uuid.UUID

class PlantLocationUpdate(SQLModel):
    reg_name: Optional[str] = None
    reg_code: Optional[str] = None
    prov_name: Optional[str] = None
    prov_code: Optional[str] = None
    mun_name: Optional[str] = None
    mun_code: Optional[str] = None
    brgy_name: Optional[str] = None
    brgy_code: Optional[str] = None
    lat: Optional[float] = None
    long: Optional[float] = None