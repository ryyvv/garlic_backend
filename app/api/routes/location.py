from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from app.core.database import get_session
from app.models.garlic import PlantLocation

router = APIRouter()

@router.get("/locations", response_model=List[PlantLocation])
async def get_locations(session: Session = Depends(get_session)):
    locations = session.exec(select(PlantLocation)).all()
    return locations

@router.post("/locations", response_model=PlantLocation)
async def create_location(location: PlantLocation, session: Session = Depends(get_session)):
    session.add(location)
    session.commit()
    session.refresh(location)
    return location