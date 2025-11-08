from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    postgres_server: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "garlic_db"
    postgres_user: str = "postgres"
    postgres_password: str = "password"
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Domain configuration
    environment: str = "development"  # development or production
    domain: str = "localhost:8002"
    production_domain: str = "api.yourdomain.com"
    
    @property
    def database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"
    
    @property
    def base_url(self) -> str:
        if self.environment == "production":
            return f"https://{self.production_domain}"
        return f"http://{self.domain}"
    
    class Config:
        env_file = ".env"

settings = Settings()