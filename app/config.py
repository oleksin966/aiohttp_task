from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    host: str
    port: int
    reload: bool

    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    class Config:
        env_file = ".env"


settings = Settings()