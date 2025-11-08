from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
from urllib.parse import quote_plus

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    
    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""
    POSTGRES_SCHEMA: str = "public"
    
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        password = quote_plus(self.POSTGRES_PASSWORD) if self.POSTGRES_PASSWORD else ""
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{password}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}?options=-csearch_path%3D{self.POSTGRES_SCHEMA}"

settings = Settings()