from peewee_async import PostgresqlDatabase
from config import settings
import os

is_docker = os.getenv('DOCKER_ENV', 'false') == 'true'

db_host = "db" if is_docker else settings.db_host

db = PostgresqlDatabase(
    settings.db_name, 
    host=db_host, 
    port=settings.db_port, 
    user=settings.db_user, 
    password=settings.db_password
)