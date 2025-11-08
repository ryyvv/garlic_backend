from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.core.database import get_session
from app.models.garlic import GarlicPlant, GarlicVariety, PlantLocation

router = APIRouter()

@router.get("/plants", response_model=List[GarlicPlant])
async def get_plants(session: Session = Depends(get_session)):
    plants = session.exec(select(GarlicPlant)).all()
    return plants

@router.post("/plants", response_model=GarlicPlant)
async def create_plant(plant: GarlicPlant, session: Session = Depends(get_session)):
    session.add(plant)
    session.commit()
    session.refresh(plant)
    return plant

@router.get("/varieties", response_model=List[GarlicVariety])
async def get_varieties(session: Session = Depends(get_session)):
    varieties = session.exec(select(GarlicVariety)).all()
    return varieties

@router.post("/varieties", response_model=GarlicVariety)
async def create_variety(variety: GarlicVariety, session: Session = Depends(get_session)):
    session.add(variety)
    session.commit()
    session.refresh(variety)
    return variety