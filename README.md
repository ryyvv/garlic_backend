# Garlic API Hub

FastAPI backend for Garlic Plant Management System.

## Setup

curl -s https://ipinfo.io/ip
always change ip

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
cp .env.example .env
```

3. Initialize database:
```bash
alembic upgrade head
```

4. Run development server:
```bash
uvicorn main:app --reload
```

## Docker

```bash
docker build -t garlic-api .
docker run -p 8000:8001 garlic-api
```

## API Endpoints

- `/` - Root endpoint
- `/health` - Health check
- `/api/auth/login` - User authentication
- `/api/garlic/plants` - Garlic plants CRUD
- `/api/location/locations` - Location management