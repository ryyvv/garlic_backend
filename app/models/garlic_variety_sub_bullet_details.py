from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class GarlicVarietySubBulletDetailsBase(SQLModel):
    variety_sub_bullet_details_id: uuid.UUID
    variety_sub_bullet_details__content: str

class GarlicVarietySubBulletDetails(GarlicVarietySubBulletDetailsBase, table=True):
    __tablename__ = "garlic_variety_sub_bullet_details"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    variety_sub_bullet_details_id: uuid.UUID
    variety_sub_bullet_details__content: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class GarlicVarietySubBulletDetailsCreate(GarlicVarietySubBulletDetailsBase):
    pass

class GarlicVarietySubBulletDetailsRead(GarlicVarietySubBulletDetailsBase):
    id: uuid.UUID

class GarlicVarietySubBulletDetailsUpdate(SQLModel):
    variety_sub_bullet_details_id: Optional[uuid.UUID] = None
    variety_sub_bullet_details__content: Optional[str] = None