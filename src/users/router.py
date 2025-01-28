from fastapi import APIRouter, status
from src.cart.services import add_user_cart
from src.users.schemas import User, UserIn
from src.users.services import create_user


users_router = APIRouter()


@users_router.post(
    path="/register", status_code=status.HTTP_201_CREATED, response_model=User
)
async def register_user(request: UserIn):
    user = await create_user(request)
    await add_user_cart(user["id"])
    return user
