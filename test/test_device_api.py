import pytest
from app.crud import create_device, get_devices, get_device, update_device, delete_device


@pytest.mark.asyncio
async def test_create_device(cli, cleanup_device):
    data = {
        'name': 'Huawei',
        'type': 'XS123',
        'login': 'testlogin',
        'password': 'testpassword',
        'location_id': 2,
        'api_user_id': 1
    }
    response = await cli.post('/create', json=data)
    assert response.status == 200
    json_response = await response.json()
    assert json_response['name'] == 'Huawei'
    assert json_response['type'] == 'XS123'
    device_id = json_response['id']
    await cleanup_device(device_id)


@pytest.mark.asyncio
async def test_get_devices(cli):
    response = await cli.get('/devices')
    assert response.status == 200
    json_response = await response.json()
    assert isinstance(json_response, list)


@pytest.mark.asyncio
async def test_get_device(cli, cleanup_device):
    device_data = {
        'name': 'Nokia',
        'type': 'X2',
        'login': 'nokialogin',
        'password': 'nokiapassword',
        'location_id': 2,
        'api_user_id': 3
    }
    post_response = await cli.post('/create', json=device_data)
    post_json = await post_response.json()
    device_id = post_json['id']

    # Get device by ID
    response = await cli.get(f'/device/{device_id}')
    assert response.status == 200
    json_response = await response.json()
    assert json_response['id'] == device_id
    assert json_response['name'] == 'Nokia'
    await cleanup_device(device_id)


@pytest.mark.asyncio
async def test_update_device(cli, cleanup_device):
    create_response = await cli.post('/create', json={
        'name': 'Test Device',
        'type': 'Android',
        'login': 'test_login',
        'password': 'test_password',
        'location_id': 1,
        'api_user_id': 1
    })
    create_data = await create_response.json()
    device_id = create_data['id']
    response = await cli.put(f'/update/{device_id}', json={
        'name': 'Updated Device',
        'type': 'iOS'
    })
    assert response.status == 200
    data = await response.json()
    assert data['name'] == 'Updated Device'
    assert data['type'] == 'iOS'
    await cleanup_device(device_id)


@pytest.mark.asyncio
async def test_delete_device(cli):
    create_response = await cli.post('/create', json={
        'name': 'Xiomi X14',
        'type': 'Android',
        'login': 'xiomi_login',
        'password': 'xiomi_password',
        'location_id': 1,
        'api_user_id': 1
    })
    create_data = await create_response.json()
    device_id = create_data['id']
    
    # Delete the device
    response = await cli.delete(f'/delete/{device_id}')
    assert response.status == 200
    data = await response.json()
    assert data['status'] == 'success'
    
    # Try to get the deleted device
    get_response = await cli.get(f'/device/{device_id}')
    assert get_response.status == 404
    get_data = await get_response.json()
    assert get_data['error'] == 'Device not found'




































