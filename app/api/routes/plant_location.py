from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
import uuid
from app.core.database import get_session
from app.models.plant_location import PlantLocation, PlantLocationCreate, PlantLocationRead, PlantLocationUpdate

router = APIRouter()

@router.get("/", response_model=List[PlantLocationRead])
async def get_locations(session: Session = Depends(get_session)):
    locations = session.exec(select(PlantLocation)).all()
    return locations

# @router.post("/data", response_model=PlantLocationRead)
# async def create_location(location: PlantLocationCreate, session: Session = Depends(get_session)):
#     db_location = PlantLocation.model_validate(location)
#     session.add(db_location)
#     session.commit()
#     session.refresh(db_location)
#     return db_location

@router.get("/{location_id}", response_model=PlantLocationRead)
async def get_location(location_id: uuid.UUID, session: Session = Depends(get_session)):
    location = session.get(PlantLocation, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.put("/{location_id}", response_model=PlantLocationRead)
async def update_location(location_id: uuid.UUID, location_update: PlantLocationUpdate, session: Session = Depends(get_session)):
    location = session.get(PlantLocation, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    
    location_data = location_update.dict(exclude_unset=True)
    for field, value in location_data.items():
        setattr(location, field, value)
    
    session.add(location)
    session.commit()
    session.refresh(location)
    return location

@router.delete("/{location_id}")
async def delete_location(location_id: uuid.UUID, session: Session = Depends(get_session)):
    location = session.get(PlantLocation, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    
    session.delete(location)
    session.commit()
    return {"message": "Location deleted"}