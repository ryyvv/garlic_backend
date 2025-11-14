from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class GarlicImagesListBase(SQLModel):
    garlic_plant_id: Optional[uuid.UUID] = None
    images_name: str
    image_result: str
    status: str

class GarlicImagesList(GarlicImagesListBase, table=True):
    __tablename__ = "garlic_images_list"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    garlic_plant_id: uuid.UUID
    images_name: str = Field(max_length=999)
    image_result: str = Field(max_length=50)
    status: str = Field(max_length=50)
    garlic_images_list_created_at: datetime = Field(default_factory=datetime.utcnow)
    garlic_images_list_updated_at: datetime = Field(default_factory=datetime.utcnow)

class GarlicImagesListCreate(GarlicImagesListBase):
    pass

class GarlicImagesListRead(GarlicImagesListBase):
    id: uuid.UUID

class GarlicImagesListUpdate(SQLModel):
    garlic_plant_id: Optional[uuid.UUID] = None
    images_name: Optional[str] = None
    image_result: Optional[str] = None
    status: Optional[str] = None