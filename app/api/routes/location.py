from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from app.core.database import get_session
from app.services.location_service import LocationService
from app.models.users import Users
from app.models.plant_location import PlantLocation

router = APIRouter()

@router.get("/search")
async def search_location(
    lat: float = Query(..., description="Latitude"),
    lng: float = Query(..., description="Longitude"),
    db: Session = Depends(get_session)
):
    try:
        location_info = await LocationService.search_location_info(lat, lng, db)
        return location_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/reverse-geocode")
async def reverse_geocode(
    lat: float = Query(..., description="Latitude"),
    lng: float = Query(..., description="Longitude")
):
    try:
        location = await LocationService.get_location_by_coordinates(lat, lng)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        return location
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user-location")
def get_user_location(
    email: str = Query(..., description="User email"),
    db: Session = Depends(get_session)
):
    try:
        statement = select(Users, PlantLocation).join(
            PlantLocation, Users.plant_location_id == PlantLocation.id
        ).where(Users.email == email)
        result = db.exec(statement).first()
        
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        
        user, plant_location = result
        return {
            "user": {
                "id": str(user.id),
                "fullname": user.fullname,
                "email": user.email,
                "birthday": user.birthday,
                "gender": user.gender,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            },
            "plant_location": {
                "id": str(plant_location.id),
                "reg_name": plant_location.reg_name,
                "reg_code": plant_location.reg_code,
                "prov_name": plant_location.prov_name,
                "prov_code": plant_location.prov_code,
                "mun_name": plant_location.mun_name,
                "mun_code": plant_location.mun_code,
                "brgy_name": plant_location.brgy_name,
                "brgy_code": plant_location.brgy_code,
                "lat": plant_location.lat,
                "long": plant_location.long
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
