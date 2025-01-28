from src.database.settings import metadata
from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table


users_roles = Table(
    "roles",
    metadata,
    Column("id", Integer, Identity(), primary_key=True, index=True),
    Column("role_name", String, nullable=False, unique=True),
)

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, Identity(), primary_key=True, index=True),
    Column("full_name", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("phone", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
    Column(
        "role",
        Integer,
        ForeignKey("roles.id", ondelete="CASCADE"),
        server_default="2",
        nullable=False,
    ),
)