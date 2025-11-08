from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
import uuid
from app.core.database import get_session
from app.models.garlic_variety_images import GarlicVarietyImages, GarlicVarietyImagesCreate, GarlicVarietyImagesRead, GarlicVarietyImagesUpdate

router = APIRouter()

@router.get("/", response_model=List[GarlicVarietyImagesRead])
async def get_variety_images(session: Session = Depends(get_session)):
    images = session.exec(select(GarlicVarietyImages)).all()
    return images

@router.post("/", response_model=GarlicVarietyImagesRead)
async def create_variety_image(image: GarlicVarietyImagesCreate, session: Session = Depends(get_session)):
    db_image = GarlicVarietyImages.from_orm(image)
    session.add(db_image)
    session.commit()
    session.refresh(db_image)
    return db_image

@router.get("/{image_id}", response_model=GarlicVarietyImagesRead)
async def get_variety_image(image_id: uuid.UUID, session: Session = Depends(get_session)):
    image = session.get(GarlicVarietyImages, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

@router.put("/{image_id}", response_model=GarlicVarietyImagesRead)
async def update_variety_image(image_id: uuid.UUID, image_update: GarlicVarietyImagesUpdate, session: Session = Depends(get_session)):
    image = session.get(GarlicVarietyImages, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    image_data = image_update.dict(exclude_unset=True)
    for field, value in image_data.items():
        setattr(image, field, value)
    
    session.add(image)
    session.commit()
    session.refresh(image)
    return image

@router.delete("/{image_id}")
async def delete_variety_image(image_id: uuid.UUID, session: Session = Depends(get_session)):
    image = session.get(GarlicVarietyImages, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    session.delete(image)
    session.commit()
    return {"message": "Image deleted"}