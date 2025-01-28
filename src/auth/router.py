from fastapi import APIRouter, status

from src.auth.exceptions import AuthRequired
from src.auth.jwt import create_access_token
from src.auth.schemas import AccessTokenResponse
from src.auth.services import authenticate_user

from src.users.schemas import AuthUser

auth_router = APIRouter()


@auth_router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=AccessTokenResponse,
    summary="User authorization endpoint",
    response_description="Grant user access token.",
)
async def login(request: AuthUser):
    user = await authenticate_user(request)
    if not user:
        raise AuthRequired()
    access_token = create_access_token(user)

    return AccessTokenResponse(access_token=access_token)