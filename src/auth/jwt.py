from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

from src.auth.config import auth_config
from src.auth.exceptions import AuthorizationFailed, AuthRequired, InvalidToken
from src.auth.schemas import TokenData
from src.auth.services import check_user_is_admin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(user: dict[str, Any], expires_delta = timedelta(minutes=auth_config.JWT_EXP)) -> str:
    jwt_data = {
        "sub": str(user["email"]),
        "exp": datetime.now(tz=timezone.utc) + expires_delta,
        "is_admin": check_user_is_admin(user),
    }

    return jwt.encode(jwt_data, auth_config.JWT_SECRET, algorithm=auth_config.JWT_ALG)


async def parse_jwt_token(
    token: str = Depends(oauth2_scheme),
) -> TokenData | None:
    if not token:
        return None

    try:
        payload = jwt.decode(
            token, auth_config.JWT_SECRET, algorithms=[auth_config.JWT_ALG]
        )
    except jwt.PyJWTError:
        raise InvalidToken()

    return TokenData(**payload)


async def parse_jwt_user_data(
    token: TokenData | None = Depends(parse_jwt_token),
) -> TokenData:
    if not token:
        raise AuthRequired()

    return token


async def parse_jwt_admin_data(
    token: TokenData = Depends(parse_jwt_user_data),
) -> TokenData:
    if not token.is_admin:
        raise AuthorizationFailed()

    return token


async def validate_admin_access(
    token: TokenData | None = Depends(parse_jwt_token),
) -> None:
    if token and token.is_admin:
        return

    raise AuthorizationFailed()