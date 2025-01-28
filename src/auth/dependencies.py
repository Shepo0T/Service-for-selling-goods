from typing import Annotated
from fastapi import Depends

from src.auth.services import get_user_by_email
from src.auth.exceptions import EmailTaken
from src.users.schemas import AuthUser


async def email(request: AuthUser) -> AuthUser:
    if await get_user_by_email(request.email):
        raise EmailTaken()

    return request


CheckEmail = Annotated[AuthUser, Depends(email)]
