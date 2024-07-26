from peewee import Model, CharField, ForeignKeyField
from db import db

class BaseModel(Model):
    class Meta:
        database = db

class ApiUser(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

class Location(BaseModel):
    name = CharField()

class Device(BaseModel):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref='devices')
    api_user = ForeignKeyField(ApiUser, backref='devices')

async def create_tables():
    with db.allow_sync():
        db.create_tables([ApiUser, Location, Device], safe=True)

    # Initialize default data (for testing device)
    default_users = [
        {"name": "ivan", "email": "ivan@gmail.com", "password": "admin"},
        {"name": "oleg", "email": "oleg@gmail.com", "password": "admin"},
        {"name": "nata", "email": "nata@gmail.com", "password": "admin"},
    ]

    default_locations = [
        {"name": "Ukraine"},
        {"name": "Germany"},
        {"name": "Poland"},
    ]

    for user_data in default_users:
        await ApiUser.get_or_create(email=user_data["email"], defaults=user_data)

    for location_data in default_locations:
        await Location.get_or_create(name=location_data["name"])
