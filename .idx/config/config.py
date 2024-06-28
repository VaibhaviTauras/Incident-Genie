from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = False 
    MASTER_DB_USER: str = "uadmin"
    MASTER_DB_PASSWORD: str = "uadmins"
    MASTER_DB_HOSTNAME: str = "localhost"
    MASTER_DB_PORT: str = "5432"
    MASTER_DB_NAME: str = "Asgard_master"
    PROFILING_ENABLED: bool = True
    

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
