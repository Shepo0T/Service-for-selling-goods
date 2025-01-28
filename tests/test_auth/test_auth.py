import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app
from src.database.settings import database, engine, metadata
from src.auth.services import create_admin, fill_roles_table

@pytest.fixture(autouse=True)
async def setup_database():
    metadata.create_all(engine)
    await database.connect()
    await fill_roles_table()
    await create_admin()
    yield
    await database.disconnect()

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.mark.anyio
async def test_login():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8000") as ac:
        # Register a test user with a unique email
        register_response = await ac.post("/api/v1/users/register", json={
            "full_name": "Test User",
            "email": "test_unique@example.com",
            "phone": "+79876543210",
            "password": "Password1!",
            "password_repeat": "Password1!"
        })
        assert register_response.status_code == 201

        # Login with the test user
        login_response = await ac.post("/api/v1/auth/login", json={
            "email": "test_unique@example.com",
            "password": "Password1!"
        })
        assert login_response.status_code == 200
        data = login_response.json()
        assert "access_token" in data