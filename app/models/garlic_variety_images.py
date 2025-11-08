from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class GarlicVarietyImagesBase(SQLModel):
    variety_id: uuid.UUID
    images_name: str
    remarks: str
    is_active: bool

class GarlicVarietyImages(GarlicVarietyImagesBase, table=True):
    __tablename__ = "garlic_variety_images"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    variety_id: uuid.UUID
    images_name: str = Field(max_length=999)
    remarks: str = Field(max_length=50)
    is_active: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class GarlicVarietyImagesCreate(GarlicVarietyImagesBase):
    pass

class GarlicVarietyImagesRead(GarlicVarietyImagesBase):
    id: uuid.UUID

class GarlicVarietyImagesUpdate(SQLModel):
    variety_id: Optional[uuid.UUID] = None
    images_name: Optional[str] = None
    remarks: Optional[str] = None
    is_active: Optional[bool] = None