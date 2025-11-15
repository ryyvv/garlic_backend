from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
import uuid
from app.core.database import get_session
from app.models.users import Users, UsersCreate, UsersRead, UsersUpdate
from app.models.garlic_plant import GarlicPlant, GarlicPlantCreate, GarlicPlantRead, GarlicPlantUpdate

router = APIRouter()


@router.get("/", response_model=List[UsersRead])
async def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(Users)).all()
    return users

@router.post("/", response_model=UsersRead)
async def create_user(user: UsersCreate, session: Session = Depends(get_session)):
    try:
        db_user = Users.model_validate(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UsersRead)
async def get_user(user_id: uuid.UUID, session: Session = Depends(get_session)):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UsersRead)
async def update_user(user_id: uuid.UUID, user_update: UsersUpdate, session: Session = Depends(get_session)):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_data = user_update.dict(exclude_unset=True)
    for field, value in user_data.items():
        setattr(user, field, value)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.delete("/{user_id}")
async def delete_user(user_id: uuid.UUID, session: Session = Depends(get_session)):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    session.delete(user)
    session.commit()
    return {"message": "User deleted"}