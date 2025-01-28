from typing import Any

from src.auth.security import hash_password
from src.database.settings import database
from src.users.models import users_table
from src.users.schemas import UserIn


async def create_user(request: UserIn) -> dict[str, Any] | None:
    query = (
        users_table.insert()
        .values(
            {
                "full_name": request.full_name,
                "email": request.email,
                "phone": request.phone,
                "password": hash_password(request.password),
            }
        )
        .returning(users_table)
    )
    return await database.fetch_one(query)