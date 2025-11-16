from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings
import os

# IAM authentication for Cloud SQL
def get_iam_token():
    """Get IAM access token for Cloud SQL authentication"""
    from google.auth import default
    from google.auth.transport.requests import Request
    credentials, project = default()
    credentials.refresh(Request())
    return credentials.token

# Connection arguments for IAM authentication
connect_args = {"connect_timeout": 30}

# Use IAM token as password when running in Cloud Run
if os.getenv("K_SERVICE") and settings.USE_IAM_AUTH:
    connect_args["password"] = get_iam_token

engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
    connect_args=connect_args
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session