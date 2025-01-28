from pydantic import BaseModel, ConfigDict


class ProductIn(BaseModel):
    name: str
    price: float
    is_active: bool


class Product(ProductIn):
    model_config = ConfigDict(from_attributes=True)
    id: int
