from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class UsersBase(SQLModel):
    fullname: str
    birthday: datetime
    email: str
    gender: str
    plant_location_id: uuid.UUID

class Users(UsersBase, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    fullname: str = Field(max_length=255)
    birthday: datetime
    email: str = Field(max_length=255)
    gender: str = Field(max_length=255)
    plant_location_id: uuid.UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UsersCreate(UsersBase):
    pass

class UsersRead(UsersBase):
    id: uuid.UUID

class UsersUpdate(SQLModel):
    fullname: Optional[str] = None
    birthday: Optional[datetime] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    plant_location_id: Optional[uuid.UUID] = None