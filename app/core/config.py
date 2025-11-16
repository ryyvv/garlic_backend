# from pydantic_settings import BaseSettings, SettingsConfigDict
# from pydantic import computed_field
# from urllib.parse import quote_plus

# class Settings(BaseSettings):
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )
    
#     # Database
#     POSTGRES_SERVER: str = "34.133.82.99"
#     POSTGRES_PORT: int = 5432
#     POSTGRES_USER: str = "postgres"
#     POSTGRES_PASSWORD: str = "Q9,[Yfh{_l_YC#_6"
#     POSTGRES_DB: str = "garlicp2"
#     POSTGRES_SCHEMA: str = "public"
    
#     @computed_field
#     @property
#     def SQLALCHEMY_DATABASE_URI(self) -> str:
#         password = quote_plus(self.POSTGRES_PASSWORD) if self.POSTGRES_PASSWORD else ""
#         return f"postgresql+psycopg://{self.POSTGRES_USER}:{password}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}?options=-csearch_path%3D{self.POSTGRES_SCHEMA}"

# settings = Settings()


import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
from urllib.parse import quote_plus

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    # App
    BASE_URL: str = "http://127.0.0.1:8000"
    ENVIRONMENT: str = "development"

    # Cloud Run
    CLOUD_RUN_URL: str = "https://garlic-api-648624765084.us-central1.run.app"

    # Database
    POSTGRES_SERVER: str = "34.133.82.99"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "Q9,[Yfh{_l_YC#_6"
    POSTGRES_DB: str = "garlicp2"
    POSTGRES_SCHEMA: str = "public"

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        password = quote_plus(self.POSTGRES_PASSWORD) if self.POSTGRES_PASSWORD else ""
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{password}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}?options=-csearch_path%3D{self.POSTGRES_SCHEMA}"

    @computed_field
    @property
    def CLOUD_RUN_URL_FINAL(self) -> str:
        return os.getenv("CLOUD_RUN_URL", self.BASE_URL)

settings = Settings()
