from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    environment: str = "development"
    project_name: str = Field(default="isrc-watcher")
    api_prefix: str = Field(default="/api")
    database_url: str = Field(..., alias="DATABASE_URL")
    pythonpath: str = Field(".", alias="PYTHONPATH")

    model_config = {
        "env_file": ".env",
        "extra": "ignore"  # Ignora variables extra no declaradas
    }

settings = Settings()