from typing import Any

from src.auth.exceptions import InvalidCredentials
from src.auth.security import check_password, hash_password
from src.database.config import settings
from src.database.settings import database
from src.users.models import users_table, users_roles
from src.users.schemas import AuthUser, User


def check_user_is_admin(user: dict[str, Any]) -> bool:
    if user["role"] == 1:
        return True
    return False


async def get_user_by_email(email: str) -> User | None:
    query = users_table.select().where(users_table.c.email == email)
    result = await database.fetch_one(query)
    if result:
        return result


async def authenticate_user(request: AuthUser) -> User:
    user = await get_user_by_email(request.email)
    if not user:
        raise InvalidCredentials()
    if not check_password(user["password"], request.password):
        raise InvalidCredentials()
    return user


async def fill_roles_table():
    query = users_roles.select()
    if not await database.fetch_one(query):
        values = [{"role_name": "admin"}, {"role_name": "user"}]
        query = users_roles.insert()
        await database.execute_many(query=query, values=values)


async def create_admin():
    query = users_table.select().where(users_table.c.role == 1)
    if not await database.fetch_one(query):
        query = users_table.insert()
        values = {
            "full_name": "Admin",
            "email": "admin@project.upit",
            "phone": "+71234567890",
            "role": 1,
            "password": hash_password(settings.ADMIN_PASSWORD),
        }
        await database.execute(query, values)
