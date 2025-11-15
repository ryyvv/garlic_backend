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
    firebase_uid: Optional[str] = Field(max_length=128, unique=True, nullable=True)

class Users(UsersBase, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    fullname: str = Field(max_length=255)
    birthday: datetime
    email: str = Field(max_length=255)
    gender: str = Field(max_length=255)
    firebase_uid: Optional[str] = Field(max_length=128, unique=True, nullable=True)
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
    firebase_uid: Optional[str] = None