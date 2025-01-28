from contextlib import asynccontextmanager


from fastapi import FastAPI

from src.auth.router import auth_router
from src.auth.services import create_admin, fill_roles_table
from src.database.settings import database, engine, metadata
from src.product.router import products_router
from src.users.router import users_router
from src.cart.router import cart_router


@asynccontextmanager
async def lifespan(_application: FastAPI):
    metadata.create_all(engine)
    await database.connect()
    await fill_roles_table()
    await create_admin()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan, root_path="/api/v1")

app.include_router(users_router, prefix="/users", tags=["Пользователи"])
app.include_router(auth_router, prefix="/auth", tags=["Аутентификация"])
app.include_router(products_router, prefix="/products", tags=["Продукты"])
app.include_router(cart_router, prefix="/cart", tags=["Корзина"])
