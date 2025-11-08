from typing import Optional, Dict, Any
import httpx
from sqlalchemy.orm import Session
from app.models.plant_location import PlantLocation

class LocationService:
    @staticmethod
    async def get_location_by_coordinates(lat: float, lng: float) -> Optional[Dict[str, Any]]:
        """
        Get location details using reverse geocoding from coordinates
        """
        try:
            # Using OpenStreetMap Nominatim API (free)
            url = f"https://nominatim.openstreetmap.org/reverse"
            params = {
                "lat": lat,
                "lon": lng,
                "format": "json",
                "addressdetails": 1
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                if data and "address" in data:
                    address = data["address"]
                    return {
                        "municipality": address.get("city") or address.get("town") or address.get("municipality"),
                        "province": address.get("state") or address.get("province"),
                        "region": address.get("region"),
                        "country": address.get("country"),
                        "full_address": data.get("display_name")
                    }
        except Exception as e:
            print(f"Error getting location: {e}")
            return None
    
    @staticmethod
    def find_nearest_location(db: Session, lat: float, lng: float) -> Optional[PlantLocation]:
        """
        Find nearest location in database using Haversine formula
        """
        # Raw SQL query to calculate distance using Haversine formula
        query = """
        SELECT *, (
            6371 * acos(
                cos(radians(:lat)) * cos(radians(lat)) * 
                cos(radians(long) - radians(:lng)) + 
                sin(radians(:lat)) * sin(radians(lat))
            )
        ) AS distance
        FROM plant_location
        ORDER BY distance
        LIMIT 1
        """
        
        result = db.execute(query, {"lat": lat, "lng": lng}).fetchone()
        if result:
            return db.query(PlantLocation).filter(PlantLocation.id == result.id).first()
        return None
    
    @staticmethod
    async def search_location_info(lat: float, lng: float, db: Session) -> Dict[str, Any]:
        """
        Combined function to get location info from API and find nearest DB location
        """
        # Get location from reverse geocoding
        api_location = await LocationService.get_location_by_coordinates(lat, lng)
        
        # Find nearest location in database
        db_location = LocationService.find_nearest_location(db, lat, lng)
        
        return {
            "coordinates": {"lat": lat, "lng": lng},
            "api_location": api_location,
            "nearest_db_location": {
                "id": str(db_location.id) if db_location else None,
                "municipality": db_location.mun_name if db_location else None,
                "province": db_location.prov_name if db_location else None,
                "region": db_location.reg_name if db_location else None,
                "barangay": db_location.brgy_name if db_location else None
            } if db_location else None
        }