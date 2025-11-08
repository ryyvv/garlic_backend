from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
import uuid
from app.core.database import get_session
from app.models.garlic_variety import GarlicVariety, GarlicVarietyCreate, GarlicVarietyRead, GarlicVarietyUpdate

router = APIRouter()

@router.get("/", response_model=List[GarlicVarietyRead])
async def get_varieties(session: Session = Depends(get_session)):
    varieties = session.exec(select(GarlicVariety)).all()
    return varieties

@router.post("/", response_model=GarlicVarietyRead)
async def create_variety(variety: GarlicVarietyCreate, session: Session = Depends(get_session)):
    db_variety = GarlicVariety.from_orm(variety)
    session.add(db_variety)
    session.commit()
    session.refresh(db_variety)
    return db_variety

@router.get("/{variety_id}", response_model=GarlicVarietyRead)
async def get_variety(variety_id: uuid.UUID, session: Session = Depends(get_session)):
    variety = session.get(GarlicVariety, variety_id)
    if not variety:
        raise HTTPException(status_code=404, detail="Variety not found")
    return variety

@router.put("/{variety_id}", response_model=GarlicVarietyRead)
async def update_variety(variety_id: uuid.UUID, variety_update: GarlicVarietyUpdate, session: Session = Depends(get_session)):
    variety = session.get(GarlicVariety, variety_id)
    if not variety:
        raise HTTPException(status_code=404, detail="Variety not found")
    
    variety_data = variety_update.dict(exclude_unset=True)
    for field, value in variety_data.items():
        setattr(variety, field, value)
    
    session.add(variety)
    session.commit()
    session.refresh(variety)
    return variety

@router.delete("/{variety_id}")
async def delete_variety(variety_id: uuid.UUID, session: Session = Depends(get_session)):
    variety = session.get(GarlicVariety, variety_id)
    if not variety:
        raise HTTPException(status_code=404, detail="Variety not found")
    
    session.delete(variety)
    session.commit()
    return {"message": "Variety deleted"}