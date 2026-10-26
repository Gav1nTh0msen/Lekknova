from pydantic import BaseModel, ConfigDict
from datetime import datetime

class FoodLogBase(BaseModel):
    servings_logged : float


class FoodLogCreate(FoodLogBase):
    food_item_id : int

class FoodLogResponse(FoodLogBase):
    id : int
    user_id : int
    food_item_id : int
    logged_at : datetime

    model_config = ConfigDict(from_attributes=True)
