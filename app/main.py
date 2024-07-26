from aiohttp import web
from watchgod import run_process
from crud import create_device, get_devices, get_device, update_device, delete_device
from db import db
from config import settings
from models import create_tables
from peewee_async import Manager
from log.log import setup_logging 

def create_app():
    app = web.Application()
    app["db"] = Manager(db)
    app.add_routes([
        web.post('/create', create_device),
        web.get('/devices', get_devices),
        web.get('/device/{device_id}', get_device),
        web.put('/update/{device_id}', update_device),
        web.delete('/delete/{device_id}', delete_device)
    ])
    return app

def start_app():
    setup_logging()
    app = create_app()
    web.run_app(app, host=settings.host, port=settings.port)

if __name__ == "__main__":
    create_tables() # Create all tables in first start
    run_process('.', start_app)



