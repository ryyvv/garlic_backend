# from pydantic_settings import BaseSettings, SettingsConfigDict
# from pydantic import computed_field
# from urllib.parse import quote_plus

# class Settings(BaseSettings):
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )
    
#     # Database
#     POSTGRES_SERVER: str = "34.10.13.136"
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


# import os
# from pydantic_settings import BaseSettings, SettingsConfigDict
# from pydantic import computed_field
# from urllib.parse import quote_plus

# class Settings(BaseSettings):
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )

#     # App
#     BASE_URL: str = "http://127.0.0.1:8000"
#     ENVIRONMENT: str = "development"

#     # Cloud Run
#     CLOUD_RUN_URL: str = "https://garlic-api-648624765084.us-central1.run.app"

#     # Database - IAM Authentication
#     POSTGRES_SERVER: str = "34.133.82.99"
#     POSTGRES_PORT: int = 5432
#     POSTGRES_USER: str = "garlic-api-sa@nicer-garlic-app.iam"
#     POSTGRES_DB: str = "garlicp2"
#     POSTGRES_SCHEMA: str = "public"
#     USE_IAM_AUTH: bool = True

#     @computed_field
#     @property
#     def SQLALCHEMY_DATABASE_URI(self) -> str:
#         # Use public IP with IAM authentication for both Cloud Run and local
#         host = os.getenv("POSTGRES_HOST", self.POSTGRES_SERVER)
#         return f"postgresql+psycopg://{self.POSTGRES_USER}:@{host}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}?options=-csearch_path%3D{self.POSTGRES_SCHEMA}"


#     @computed_field
#     @property
#     def CLOUD_RUN_URL_FINAL(self) -> str:
#         return os.getenv("CLOUD_RUN_URL", self.BASE_URL)

# settings = Settings()


import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
from urllib.parse import quote_plus

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # App
    BASE_URL: str = "http://127.0.0.1:8000"
    ENVIRONMENT: str = "development"

    # Cloud Run URL
    CLOUD_RUN_URL: str = "https://garlic-api-648624765084.us-central1.run.app"

    # Database - IAM Authentication
    POSTGRES_USER: str = "garlic-api-sa@nicer-garlic-app.iam"
    POSTGRES_DB: str = "garlicp2"
    POSTGRES_SCHEMA: str = "public"
    INSTANCE_CONNECTION_NAME: str = "nicer-garlic-app:us-central1:dev-nicergarlic-pg"

    # Local development (non-IAM)
    LOCAL_DB_HOST: str = "34.10.13.136"
    LOCAL_DB_USER: str = "postgres"
    LOCAL_DB_PASSWORD: str = "Q9,[Yfh{_l_YC#_6"

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        """
        Cloud Run → use Cloud SQL Unix socket + IAM
        Local machine → use public IP + password
        """

        if os.getenv("K_SERVICE"):  # Running inside Cloud Run
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}@/"
                f"{self.POSTGRES_DB}"
                f"?host=/cloudsql/{self.INSTANCE_CONNECTION_NAME}"
                f"&options=-csearch_path%3D{self.POSTGRES_SCHEMA}"
            )

        # Local dev using Public IP
        password = quote_plus(self.LOCAL_DB_PASSWORD)
        return (
            f"postgresql+asyncpg://{self.LOCAL_DB_USER}:{password}"
            f"@{self.LOCAL_DB_HOST}:5432/{self.POSTGRES_DB}"
            f"?options=-csearch_path%3D{self.POSTGRES_SCHEMA}"
        )

    @computed_field
    @property
    def CLOUD_RUN_URL_FINAL(self) -> str:
        return os.getenv("CLOUD_RUN_URL", self.CLOUD_RUN_URL)

settings = Settings()
