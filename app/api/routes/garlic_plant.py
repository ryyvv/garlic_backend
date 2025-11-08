from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
import uuid
from app.core.database import get_session
from app.models.garlic_plant import GarlicPlant, GarlicPlantCreate, GarlicPlantRead, GarlicPlantUpdate

router = APIRouter()

@router.get("/", response_model=List[GarlicPlantRead])
async def get_plants(session: Session = Depends(get_session)):
    plants = session.exec(select(GarlicPlant)).all()
    return plants

@router.post("/", response_model=GarlicPlantRead)
async def create_plant(plant: GarlicPlantCreate, session: Session = Depends(get_session)):
    db_plant = GarlicPlant.from_orm(plant)
    session.add(db_plant)
    session.commit()
    session.refresh(db_plant)
    return db_plant

@router.get("/{plant_id}", response_model=GarlicPlantRead)
async def get_plant(plant_id: uuid.UUID, session: Session = Depends(get_session)):
    plant = session.get(GarlicPlant, plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    return plant

@router.put("/{plant_id}", response_model=GarlicPlantRead)
async def update_plant(plant_id: uuid.UUID, plant_update: GarlicPlantUpdate, session: Session = Depends(get_session)):
    plant = session.get(GarlicPlant, plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    
    plant_data = plant_update.dict(exclude_unset=True)
    for field, value in plant_data.items():
        setattr(plant, field, value)
    
    session.add(plant)
    session.commit()
    session.refresh(plant)
    return plant

@router.delete("/{plant_id}")
async def delete_plant(plant_id: uuid.UUID, session: Session = Depends(get_session)):
    plant = session.get(GarlicPlant, plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    
    session.delete(plant)
    session.commit()
    return {"message": "Plant deleted"}