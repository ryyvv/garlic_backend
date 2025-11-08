from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class GarlicVarietyCategoryBulletDetailsBase(SQLModel):
    variety_category_bullet_details_id: uuid.UUID
    variety_category_bullet_details_name: str

class GarlicVarietyCategoryBulletDetails(GarlicVarietyCategoryBulletDetailsBase, table=True):
    __tablename__ = "garlic_variety_category_bullet_details"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    variety_category_bullet_details_id: uuid.UUID
    variety_category_bullet_details_name: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class GarlicVarietyCategoryBulletDetailsCreate(GarlicVarietyCategoryBulletDetailsBase):
    pass

class GarlicVarietyCategoryBulletDetailsRead(GarlicVarietyCategoryBulletDetailsBase):
    id: uuid.UUID

class GarlicVarietyCategoryBulletDetailsUpdate(SQLModel):
    variety_category_bullet_details_id: Optional[uuid.UUID] = None
    variety_category_bullet_details_name: Optional[str] = None