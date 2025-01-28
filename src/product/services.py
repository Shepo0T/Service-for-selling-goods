from datetime import datetime, timezone
from typing import Any

from src.database.settings import database
from src.product.models import products_table
from src.product.schemas import ProductIn, Product


async def create_product(request: ProductIn) -> dict[str, Any]:
    query = (
        products_table.insert()
        .values(
            {
                "name": request.name,
                "price": request.price,
                "is_active": request.is_active,
            }
        )
        .returning(products_table)
    )
    return await database.fetch_one(query)


async def remove_product(product_id: int):
    query = products_table.delete().where(products_table.c.id == product_id)
    await database.execute(query)


async def edit_product(product_id: int, request: ProductIn):
    query = (
        products_table.update()
        .where(products_table.c.id == product_id)  # request.id
        .values(
            {
                "name": request.name,
                "price": request.price,
                "is_active": request.is_active,
                "updated_at": datetime.now(tz=timezone.utc),
            }
        )
    ).returning(products_table)
    return await database.fetch_one(query)


async def get_product(product_id: int) -> Product:
    query = products_table.select().where(products_table.c.id == product_id)
    return await database.fetch_one(query)
