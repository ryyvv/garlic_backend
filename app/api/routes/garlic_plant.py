from typing import List
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError, DataError, ProgrammingError
from sqlmodel import select, Session

from app.core.database import get_session
from app.models.garlic_plant import GarlicPlant, GarlicPlantCreate, GarlicPlantRead, GarlicPlantUpdate

router = APIRouter()

@router.get("/", response_model=List[GarlicPlantRead])
def get_plants(session: Session = Depends(get_session)):
    """Get all garlic plants"""
    statement = select(GarlicPlant)
    plants = session.exec(statement).all()
    return plants

@router.post("/", response_model=GarlicPlantRead, status_code=201)
def create_plant(plant: GarlicPlantCreate, session: Session = Depends(get_session)):
    """Create a new garlic plant"""
    try:
        db_plant = GarlicPlant.model_validate(plant)
        session.add(db_plant)
        session.commit()
        session.refresh(db_plant)
        return db_plant
    except (IntegrityError, DataError, ProgrammingError) as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{plant_id}", response_model=GarlicPlantRead)
def get_plant(plant_id: uuid.UUID, session: Session = Depends(get_session)):
    """Get a specific garlic plant by ID"""
    plant = session.get(GarlicPlant, plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    return plant

@router.put("/{plant_id}", response_model=GarlicPlantRead)
def update_plant(plant_id: uuid.UUID, plant_update: GarlicPlantUpdate, session: Session = Depends(get_session)):
    """Update a garlic plant"""
    plant = session.get(GarlicPlant, plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    
    try:
        plant_data = plant_update.model_dump(exclude_unset=True)
        for field, value in plant_data.items():
            setattr(plant, field, value)
        
        session.add(plant)
        session.commit()
        session.refresh(plant)
        return plant
    except (IntegrityError, DataError, ProgrammingError) as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{plant_id}", status_code=204)
def delete_plant(plant_id: uuid.UUID, session: Session = Depends(get_session)):
    """Delete a garlic plant"""
    plant = session.get(GarlicPlant, plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    
    session.delete(plant)
    session.commit()
    return None