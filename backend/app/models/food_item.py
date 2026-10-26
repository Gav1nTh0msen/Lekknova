from datetime import datetime
from sqlalchemy import Float, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class FoodItem(Base):
    __tablename__ = "food_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    
    serving_unit: Mapped[str] = mapped_column(
        String, nullable=False, default="serving"
    )  # ex: "g", "oz", "egg", "scoop"

    # Base Nutritional Values (per 1 unit)
    calories: Mapped[float] = mapped_column(Float, nullable=False)
    protein: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    carbs: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    fat: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    logs: Mapped[list["FoodLog"]] = relationship(
        "FoodLog", back_populates="food_item", cascade="all, delete-orphan"
    )
