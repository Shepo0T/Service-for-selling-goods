from fastapi import APIRouter, Depends, status

from src.auth.jwt import parse_jwt_admin_data
from src.product.schemas import Product, ProductIn
from src.product.services import create_product, edit_product, remove_product

products_router = APIRouter()


@products_router.post(
    path="/create",
    status_code=status.HTTP_201_CREATED,
    response_model=Product,
    dependencies=[Depends(parse_jwt_admin_data)],
)
async def add_product(request: ProductIn):
    product = await create_product(request)
    return product


@products_router.put(
    path="/update/{product_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(parse_jwt_admin_data)],
)
async def update_product(product_id: int, request: ProductIn):
    product = await edit_product(product_id, request)
    return product


@products_router.delete(
    path="/delete/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(parse_jwt_admin_data)],
)
async def delete_product(product_id: int):
    await remove_product(product_id)
