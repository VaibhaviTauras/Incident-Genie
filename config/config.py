from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = False
    APP_ENV: str
    PROFILING_ENABLED: bool = False
    SERVICE_NAME: str
    SERVICE_ID: int
    MASTER_DB_USER: str
    MASTER_DB_PASSWORD: str
    MASTER_DB_HOSTNAME: str
    MASTER_DB_PORT: str
    MASTER_DB_NAME: str


    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
