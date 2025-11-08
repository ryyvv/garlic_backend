import requests

try:
    response = requests.get('https://ipinfo.io/ip')
    print(f"Your public IP: {response.text.strip()}")
    print("Add this IP to Google Cloud SQL Authorized Networks")
except Exception as e:
    print(f"Error getting IP: {e}")