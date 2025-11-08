from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class GarlicPlantBase(SQLModel):
    garlic_title: Optional[str] = None
    variety_id: uuid.UUID
    plant_location_id: uuid.UUID
    image_name: uuid.UUID
    status: str
    is_active: bool

class GarlicPlant(GarlicPlantBase, table=True):
    __tablename__ = "garlic_plant"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    garlic_title: Optional[str] = Field(default=None, max_length=255)
    variety_id: uuid.UUID
    plant_location_id: uuid.UUID
    image_name: uuid.UUID
    status: str = Field(max_length=50)
    is_active: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class GarlicPlantCreate(GarlicPlantBase):
    pass

class GarlicPlantRead(GarlicPlantBase):
    id: uuid.UUID

class GarlicPlantUpdate(SQLModel):
    garlic_title: Optional[str] = None
    variety_id: Optional[uuid.UUID] = None
    plant_location_id: Optional[uuid.UUID] = None
    image_name: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None