from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from app.config.settings import JWT_SECRET_KEY, JWT_ALGORITHM

security = HTTPBearer(auto_error=False)


async def get_user_identifier(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
):
    """
    JWT token'dan kullanıcı kimliğini çıkarır.
    Token yoksa anonim kullanıcı olarak işaretler.
    """
    if credentials is None:
        return "global_unauthenticated_user"

    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
