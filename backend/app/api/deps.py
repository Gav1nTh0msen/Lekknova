from typing import AsyncGenerator
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.config import settings
from app.db.session import AsyncSessionLocal, get_db
from app.models.user import User

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)


async def get_current_user(
    db: AsyncSession = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> User:
     credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
     try:
         token_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
         user_id: str | None = token_payload.get("sub")
         if user_id is None:
              raise credentials_exception
     except jwt.PyJWTError:
          raise credentials_exception
     result = await db.execute(select(User).where(User.id == int(user_id)))
     user = result.scalars().first()
     if user is None:
          raise credentials_exception
     return user
