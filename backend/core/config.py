from pathlib import Path
from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class SuperUser(BaseModel):
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.tempalte.", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )
    run: RunConfig = RunConfig()
    db: DataBaseConfig
    access_token: AccessToken
    superuser: SuperUser


settings = Settings()  # type: ignore
