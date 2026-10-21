from datetime import datetime, timezone
from sqlalchemy import Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class FoodLog(Base) :
    __tablename__ = "food_logs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    food_item_id: Mapped[int] = mapped_column( ForeignKey("food_items.id", ondelete="CASCADE"), index=True, nullable=False)
    servings_logged: Mapped[float] = mapped_column(Float, nullable=False)
    
    logged_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    user: Mapped["User"] = relationship("User", back_populates="logs")
    food_item: Mapped["FoodItem"] = relationship("FoodItem", back_populates="logs")
