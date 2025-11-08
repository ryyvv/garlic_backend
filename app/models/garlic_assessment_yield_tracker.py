from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from uuid import UUID, uuid4
from decimal import Decimal

if TYPE_CHECKING:
    from .garlic_plant import GarlicPlant

class GarlicAssessmentYieldTracker(SQLModel, table=True):
    __tablename__ = "garlic_assesment-yield-tracker"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    garlic_plant_task_id: UUID = Field(foreign_key="garlic_plant.id")
    harvest_date: datetime
    grand_total_kg: float
    subtotal_small_kg: Optional[float] = None
    subtotal_medium_kg: Optional[float] = None
    subtotal_large_kg: Optional[float] = None
    percent_small_bulb: Optional[float] = None
    percent_medium_bulb: Optional[float] = None
    percent_large_bulb: Optional[float] = None
    total_expenses: Optional[Decimal] = None
    market_price_per_kg: Optional[Decimal] = None
    gross_income: Optional[Decimal] = None
    net_profit: Optional[Decimal] = None
    profit_margin: Optional[float] = None
    farmer_satisfaction_rating: Optional[str] = Field(max_length=50)
    farmer_feedback: Optional[str] = Field(max_length=999)
    remarks: Optional[str] = Field(max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    garlic_plant: "GarlicPlant" = Relationship(back_populates="yield_trackers")