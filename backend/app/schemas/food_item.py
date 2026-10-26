from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class FoodItemBase(BaseModel):
    name : str
    serving_unit : str = "serving"
    calories : float
    protein : float = 0.0
    carbs : float = 0.0
    fat: float = 0.0


class FoodItemCreate(FoodItemBase):
    pass

class FoodItemResponse(FoodItemBase):
    id : int
    created_at : datetime

    model_config = ConfigDict(from_attributes=True)
