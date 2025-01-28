from sqlalchemy import Table, Integer, Column, Identity, ForeignKey, DECIMAL
from src.database.settings import metadata


# Таблица для хранения корзин пользователей
carts_table = Table(
    "shopping_carts",
    metadata,
    Column("id", Integer, Identity(), index=True, primary_key=True),
    Column("owner", ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
)

# Таблица для хранения продуктов в корзинах
product_carts_table = Table(
    "product_shopping_carts",
    metadata,
    Column("id", Integer, Identity(), primary_key=True, index=True),
    Column(
        "cart_id",
        ForeignKey("shopping_carts.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    ),
    Column("product_id", ForeignKey("products.id", ondelete="CASCADE"), nullable=False),
    Column("quantity", Integer),
    Column("total_price", DECIMAL, nullable=False),
)