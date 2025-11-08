import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_SERVER"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        connect_timeout=10
    )
    print("✅ Database connection successful!")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print(f"Host: {os.getenv('POSTGRES_SERVER')}")
    print(f"Port: {os.getenv('POSTGRES_PORT')}")
    print(f"Database: {os.getenv('POSTGRES_DB')}")
    print(f"User: {os.getenv('POSTGRES_USER')}")
    print(f"Password: {'*' * len(os.getenv('POSTGRES_PASSWORD', ''))}")