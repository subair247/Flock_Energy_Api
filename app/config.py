from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    base_url: str = "https://urja-ops.flockenergy.tech"
    default_username: str = "operator@urja.local"
    default_password: str = "urja-ops-2026"

    class Config:
        env_file = ".env"

settings = Settings()