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
#for local to pc
uvicorn main:app --reload --host 192.168.8.132 --port 8000

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



    Variety
    "id": 977684a2-2c39-4b4e-989c-210643e5bab9

    location:
    "id": 5747d911-c532-466a-86f6-ce13bf6224d7

    user : 4ed21bca-1287-4d96-9e65-9753c2090614

[
  {
    "fullname": "Ryan James",
    "birthday": "2025-11-15T04:48:59.131000",
    "email": "priany19@gmail.com",
    "gender": "Male",
    "firebase_uid": "DDLaq6J2DGR68XLnjrDmj9Bfpkk2",
    "id": "25248f7c-a75b-4b34-a907-fce2eecc1bfa"
  }
]