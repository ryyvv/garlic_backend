from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    pool_size=20,
    max_overflow=30,
    pool_timeout=60,
    pool_recycle=1800,
    pool_pre_ping=True,
    connect_args={
        "connect_timeout": 30,
    }
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session