from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
import uuid
from app.core.database import get_session
from app.models.garlic_variety_sub_bullet_details import GarlicVarietySubBulletDetails, GarlicVarietySubBulletDetailsCreate, GarlicVarietySubBulletDetailsRead, GarlicVarietySubBulletDetailsUpdate

router = APIRouter()

@router.get("/", response_model=List[GarlicVarietySubBulletDetailsRead])
async def get_sub_bullets(session: Session = Depends(get_session)):
    items = session.exec(select(GarlicVarietySubBulletDetails)).all()
    return items

@router.post("/", response_model=GarlicVarietySubBulletDetailsRead)
async def create_sub_bullet(item: GarlicVarietySubBulletDetailsCreate, session: Session = Depends(get_session)):
    db_item = GarlicVarietySubBulletDetails.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@router.get("/{item_id}", response_model=GarlicVarietySubBulletDetailsRead)
async def get_sub_bullet(item_id: uuid.UUID, session: Session = Depends(get_session)):
    item = session.get(GarlicVarietySubBulletDetails, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=GarlicVarietySubBulletDetailsRead)
async def update_sub_bullet(item_id: uuid.UUID, item_update: GarlicVarietySubBulletDetailsUpdate, session: Session = Depends(get_session)):
    item = session.get(GarlicVarietySubBulletDetails, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item_data = item_update.dict(exclude_unset=True)
    for field, value in item_data.items():
        setattr(item, field, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.delete("/{item_id}")
async def delete_sub_bullet(item_id: uuid.UUID, session: Session = Depends(get_session)):
    item = session.get(GarlicVarietySubBulletDetails, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    session.delete(item)
    session.commit()
    return {"message": "Item deleted"}