from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
import uuid
from app.core.database import get_session
from app.models.garlic_variety_category_bullet_details import GarlicVarietyCategoryBulletDetails, GarlicVarietyCategoryBulletDetailsCreate, GarlicVarietyCategoryBulletDetailsRead, GarlicVarietyCategoryBulletDetailsUpdate

router = APIRouter()

@router.get("/", response_model=List[GarlicVarietyCategoryBulletDetailsRead])
async def get_category_bullets(session: Session = Depends(get_session)):
    items = session.exec(select(GarlicVarietyCategoryBulletDetails)).all()
    return items

@router.post("/", response_model=GarlicVarietyCategoryBulletDetailsRead)
async def create_category_bullet(item: GarlicVarietyCategoryBulletDetailsCreate, session: Session = Depends(get_session)):
    db_item = GarlicVarietyCategoryBulletDetails.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@router.get("/{item_id}", response_model=GarlicVarietyCategoryBulletDetailsRead)
async def get_category_bullet(item_id: uuid.UUID, session: Session = Depends(get_session)):
    item = session.get(GarlicVarietyCategoryBulletDetails, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=GarlicVarietyCategoryBulletDetailsRead)
async def update_category_bullet(item_id: uuid.UUID, item_update: GarlicVarietyCategoryBulletDetailsUpdate, session: Session = Depends(get_session)):
    item = session.get(GarlicVarietyCategoryBulletDetails, item_id)
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
async def delete_category_bullet(item_id: uuid.UUID, session: Session = Depends(get_session)):
    item = session.get(GarlicVarietyCategoryBulletDetails, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    session.delete(item)
    session.commit()
    return {"message": "Item deleted"}