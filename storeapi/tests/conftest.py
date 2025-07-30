from typing import Generator,AsyncGenerator
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from httpx import ASGITransport

from storeapi.main import app
from storeapi.routers.post import post_table,comment_table

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture()
def client()->Generator:
    yield TestClient(app)

@pytest.fixture(autouse=True)
async def db()->AsyncGenerator:
    post_table.clear()
    comment_table.clear()

@pytest.fixture()
async def async_client(client)->AsyncGenerator:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport,base_url=client.base_url) as ac:
        yield ac


