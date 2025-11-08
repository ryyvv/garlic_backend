from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4

class GarlicVariety(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    variety_name: str
    variety_description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class PlantLocation(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
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

class GarlicPlant(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: Optional[str] = None
    plant_location_id: UUID = Field(foreign_key="plantlocation.id")
    image_name: str
    date_harvest: datetime
    status: bool = True
    harvest_status: str
    variety_id: UUID = Field(foreign_key="garlicvariety.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)