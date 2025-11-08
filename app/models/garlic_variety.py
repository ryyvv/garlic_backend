from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class GarlicVarietyBase(SQLModel):
    variety_name: str
    variety_description: Optional[str] = None

class GarlicVariety(GarlicVarietyBase, table=True):
    __tablename__ = "garlic_variety"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    variety_name: str = Field(max_length=50)
    variety_description: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class GarlicVarietyCreate(GarlicVarietyBase):
    pass

class GarlicVarietyRead(GarlicVarietyBase):
    id: uuid.UUID

class GarlicVarietyUpdate(SQLModel):
    variety_name: Optional[str] = None
    variety_description: Optional[str] = None