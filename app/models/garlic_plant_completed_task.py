from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class GarlicPlantCompletedTaskBase(SQLModel):
    garlic_plant_task_id: uuid.UUID
    completed_task_name: str
    completed_task_remarks: str
    completed_task_date: datetime
    completed_task_type: str
    completed_task_status: str

class GarlicPlantCompletedTask(GarlicPlantCompletedTaskBase, table=True):
    __tablename__ = "garlic_plant_completed_task"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    garlic_plant_task_id: uuid.UUID = Field(foreign_key=f"{os.getenv('POSTGRES_SCHEMA')}.garlic_plant.id")
    completed_task_name: str = Field(max_length=255)
    completed_task_remarks: str = Field(max_length=255)
    completed_task_date: datetime
    completed_task_type: str = Field(max_length=50)
    completed_task_status: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class GarlicPlantCompletedTaskCreate(GarlicPlantCompletedTaskBase):
    pass

class GarlicPlantCompletedTaskRead(GarlicPlantCompletedTaskBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class GarlicPlantCompletedTaskUpdate(SQLModel):
    garlic_plant_task_id: Optional[uuid.UUID] = None
    completed_task_name: Optional[str] = None
    completed_task_remarks: Optional[str] = None
    completed_task_date: Optional[datetime] = None
    completed_task_type: Optional[str] = None
    completed_task_status: Optional[str] = None