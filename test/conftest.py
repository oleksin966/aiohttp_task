import pytest
import asyncio
from peewee_async import Manager
from app.crud import create_device, get_devices, get_device, update_device, delete_device
from app.main import create_app
from app.db import db
from app.models import Device


@pytest.fixture(scope='module')
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def cli(event_loop, aiohttp_client):
    app = create_app()
    app.router.add_post('/create', create_device)
    app.router.add_get('/devices', get_devices)
    app.router.add_get('/device/{device_id}', get_device)
    app.router.add_put('/update/{device_id}', update_device)
    app.router.add_delete('/delete/{device_id}', delete_device)
    return event_loop.run_until_complete(aiohttp_client(app))


@pytest.fixture
async def cleanup_device():
    async def _cleanup(device_id):
        await Manager(db).execute(Device.delete().where(Device.id == device_id))
        await Manager(db).close()
    return _cleanup