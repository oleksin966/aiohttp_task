# aiohttp_task
## Prerequisites

Before starting the application, ensure you have the following installed:

- Python (version 3.10)
- Pip (version 22.0.2)
- Postgresql (version 14.12)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/oleksin966/aiohttp_task
    ```

2. Navigate to the project directory:
    ```bash
    cd aiohttp_task
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix/Mac
    # or
    .\venv\Scripts\activate   # For Windows
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Environment Variables**

	Create a `.env` file in the project root directory. This file will store environment variables required for the application.

	Example `.env.sample` file:
	```ini
	app_name=aiohttp
	host=0.0.0.0
	port=8080
	reload=True

	db_host=0.0.0.0
	db_port=5432
	db_user=postgres
	db_password=admin
	db_name=aiohttp
	```

   Replace the placeholder values with your actual configuration.

## Running the Application

1. To start the application, run the following command:
```bash
python app/main.py
```

## Running test

1. To start the test, run the following command:
```bash
pytest test/
```

## Running the Application with Docker Compose

1. Make sure to configure your environment by creating a .env file with the required variables before running Docker Compose.

To build and start the application using Docker Compose, run the following command:
```bash
docker-compose up --build
```

For subsequent runs, you can use:
```bash
docker-compose up
```

You can access the API endpoints using a web browser.

## API Testing with cURL

1. To create a new device, use the following cURL command:
**Create Device**

```bash
curl -X POST http://0.0.0.0:8080/create \
-H "Content-Type: application/json" \
-d '{
    "name": "Device1",
    "type": "Sensor",
    "login": "device_login",
    "password": "device_password",
    "location_id": 1,
    "api_user_id": 1
}'
```

**Retrieve All Devices**
2. To retrieve a list of all devices, use the following cURL command:

```bash
curl -X GET http://0.0.0.0:8080/devices
```

**Retrieve a Single Device**
3. To retrieve a single device by its ID, use the following cURL command (replace <device_id> with the actual device ID):

```bash
curl -X GET http://0.0.0.0:8080/device/<device_id>
```

**Update Device**
4. To update an existing device, use the following cURL command (replace <device_id> with the actual device ID):

```bash
curl -X PUT http://0.0.0.0:8080/update/<device_id> \
-H "Content-Type: application/json" \
-d '{
    "name": "UpdatedDeviceName",
    "type": "UpdatedType"
}'
```

**Delete Device**
5. To delete a device by its ID, use the following cURL command (replace <device_id> with the actual device ID):

```bash
curl -X DELETE http://0.0.0.0:8080/delete/<device_id>
```

Ensure that the server is running and listening on the specified port before executing these commands. Adjust the port and hostname as needed based on your configuration.