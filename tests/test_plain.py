from async_asgi_testclient import TestClient
from myapp import main
import pytest, json

@pytest.mark.asyncio
async def test_willpyre_app():

    async with TestClient(main) as client:
        resp = await client.get("/")
        assert resp.status_code == 200
        assert resp.text == "index page"

@pytest.mark.asyncio
async def test_willpyre_post():

    async with TestClient(main) as client:
        resp = await client.post("/login/", data="a=anything")
        assert resp.status_code == 200
        assert resp.text == "anything"

@pytest.mark.asyncio
async def test_willpyre_get():

    async with TestClient(main) as client:
        resp = await client.get("/login/?user=admin")
        assert resp.status_code == 200
        assert resp.text == "Welcome admin"

@pytest.mark.asyncio
async def test_trailing_slash():

    async with TestClient(main) as client:
        resp = await client.get("/login")
        assert resp.status_code == 200
        assert resp.text == "Welcome ordinary user"

@pytest.mark.asyncio
async def test_url_vars():

    async with TestClient(main) as client:
        resp = await client.get("/api/hello")
        assert resp.status_code == 200
        assert resp.text == "You requested the variable hello"

@pytest.mark.asyncio
async def test_utils():

    async with TestClient(main) as client:
        resp = await client.get("/json")
        assert resp.json() == {'a':'b'}
        assert resp.headers["Content-Type"] == "application/json"