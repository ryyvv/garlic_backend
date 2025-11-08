from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel
import uuid
import os
from datetime import datetime

class GarlicWeatherForecastLogsBase(SQLModel):
    garlic_plant_id: uuid.UUID
    weather_forecast_today_log_ave_temp: str
    weather_forecast_today_log_min_temp: str
    weather_forecast_today_log_max_temp: str
    weather_forecast_today_log_humidity: str
    weather_forecast_today_log_wind: str
    weather_forecast_today_log_preipitation: str
    weather_forecast_today_log_sunrise: str
    weather_forecast_today_log_sunset: str
    weather_forecast_status: str

class GarlicWeatherForecastLogs(GarlicWeatherForecastLogsBase, table=True):
    __tablename__ = "garlic_weather_forecast-logs"
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    garlic_plant_id: uuid.UUID = Field(foreign_key=f"{os.getenv('POSTGRES_SCHEMA')}.garlic_plant.id")
    weather_forecast_today_log_ave_temp: str = Field(max_length=50)
    weather_forecast_today_log_min_temp: str = Field(max_length=50)
    weather_forecast_today_log_max_temp: str = Field(max_length=50)
    weather_forecast_today_log_humidity: str = Field(max_length=50)
    weather_forecast_today_log_wind: str = Field(max_length=50)
    weather_forecast_today_log_preipitation: str = Field(max_length=50)
    weather_forecast_today_log_sunrise: str = Field(max_length=50)
    weather_forecast_today_log_sunset: str = Field(max_length=50)
    weather_forecast_status: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class GarlicWeatherForecastLogsCreate(GarlicWeatherForecastLogsBase):
    pass

class GarlicWeatherForecastLogsRead(GarlicWeatherForecastLogsBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class GarlicWeatherForecastLogsUpdate(SQLModel):
    garlic_plant_id: Optional[uuid.UUID] = None
    weather_forecast_today_log_ave_temp: Optional[str] = None
    weather_forecast_today_log_min_temp: Optional[str] = None
    weather_forecast_today_log_max_temp: Optional[str] = None
    weather_forecast_today_log_humidity: Optional[str] = None
    weather_forecast_today_log_wind: Optional[str] = None
    weather_forecast_today_log_preipitation: Optional[str] = None
    weather_forecast_today_log_sunrise: Optional[str] = None
    weather_forecast_today_log_sunset: Optional[str] = None
    weather_forecast_status: Optional[str] = None