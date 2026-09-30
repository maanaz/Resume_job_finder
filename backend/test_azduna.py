import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

params = {
    "app_id": os.getenv("ADZUNA_ID"),
    "app_key": os.getenv("ADZUNA_KEY"),
    "what": "Python Developer",
    "where": "Bangalore",
    "results_per_page": 5
}

response = requests.get(url, params=params)

print("STATUS:", response.status_code)
print(response.text[:3000])