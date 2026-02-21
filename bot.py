import requests
from datetime import datetime

SUPABASE_URL = "https://aonegynruldsjvpttret.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFvbmVneW5ydWxkc2p2cHR0cmV0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTUwODYyOCwiZXhwIjoyMDg3MDg0NjI4fQ.V1RpSYErIiZYVhGIopcoO3TrUlQLaq0Wate9VKrDw4M"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "resolution=merge-duplicates"
}

def upload_vehicle(data):
    url = f"{SUPABASE_URL}/rest/v1/vehicles"
    params = {
        "on_conflict": "brand,model,variant"
    }
    response = requests.post(
        url,
        headers=HEADERS,
        params=params,
        json=data
    )
    print(response.status_code, response.text)
vehicle_data = {
    "type": "bike",
    "brand": "Yamaha",
    "model": "R15",
    "variant": "V4",
    "engine": "155cc",
    "power": "18.4 PS",
    "fuel": "Petrol",
    "transmission": "Manual",
    "price_inr": 180000,
    "source_name": "Yamaha India",
    "source_url": "https://www.yamaha-motor-india.com",
    "last_updated": datetime.now().isoformat()
}

upload_vehicle(vehicle_data)
