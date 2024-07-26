from aiohttp import web
from db import db
from models import Device
from peewee import DoesNotExist
import logging

db.set_allow_sync(False)

logger = logging.getLogger(__name__)

def format_device_data(device):
    return {
        'id': device.id,
        'name': device.name,
        'type': device.type,
        'login': device.login,
        'password': device.password,
        'location_id': device.location_id,
        'api_user_id': device.api_user_id
    }

async def create_device(request):
    db = request.app['db']
    try:
        data = await request.json()
        logger.debug(f"Creating device with data: {data}")
        device = await db.create(Device, **data)
        logger.info(f"Device created with ID: {device.id}")
        return web.json_response(format_device_data(device))
    except KeyError as e:
        logger.error(f"Missing field: {str(e)}")
        return web.json_response({'error': f'Missing field: {str(e)}'}, status=400)
    except Exception as e:
        logger.error("Exception occurred while creating device")
        return web.json_response({'error': str(e)}, status=500)

async def get_devices(request):
    db = request.app['db']
    try:
        devices = await db.execute(Device.select())
        logger.info(f"Retrieved {len(devices)} devices")
        return web.json_response([format_device_data(device) for device in devices])
    except Exception as e:
        logger.error("Exception occurred while retrieving devices")
        return web.json_response({'error': str(e)}, status=500)

async def get_device(request):
    db = request.app['db']
    device_id = int(request.match_info['device_id'])
    try:
        device = await db.get(Device, id=device_id)
        logger.info(f"Retrieved device with ID: {device.id}")
        return web.json_response(format_device_data(device))
    except DoesNotExist:
        logger.warning(f"Device with ID {device_id} not found")
        return web.json_response({'error': 'Device not found'}, status=404)
    # except Exception as e:
    #     logger.error("Exception occurred while retrieving device")
    #     return web.json_response({'error': str(e)}, status=500)

async def update_device(request):
    db = request.app['db']
    device_id = int(request.match_info['device_id'])
    try:
        data = await request.json()
        if not any(key in data for key in ['name', 'type', 'login', 'password', 'location_id', 'api_user_id']):
            raise KeyError('At least one field to update is required')
        
        logger.debug(f"Updating device with ID {device_id} with data: {data}")
        query = Device.update(**data).where(Device.id == device_id)
        await db.execute(query)

        device = await db.get(Device, id=device_id)
        logger.info(f"Device with ID {device_id} updated")
        return web.json_response(format_device_data(device))
    except DoesNotExist:
        logger.warning(f"Device with ID {device_id} not found")
        return web.json_response({'error': 'Device not found'}, status=404)
    except KeyError as e:
        logger.error(f"Invalid field: {str(e)}")
        return web.json_response({'error': f'Invalid field: {str(e)}'}, status=400)
    except Exception as e:
        logger.error("Exception occurred while updating device")
        return web.json_response({'error': str(e)}, status=500)

async def delete_device(request):
    db = request.app['db']
    device_id = int(request.match_info['device_id'])
    try:
        logger.debug(f"Deleting device with ID: {device_id}")
        device = await db.execute(Device.delete().where(Device.id == device_id))
        if device == 0:
            logger.warning(f"Device with ID {device_id} not found for deletion")
            return web.json_response({'error': 'Device not found'}, status=404)
        logger.info(f"Device with ID {device_id} deleted")
        return web.json_response({'status': 'success'})
    except Exception as e:
        logger.error("Exception occurred while deleting device")
        return web.json_response({'error': str(e)}, status=500)