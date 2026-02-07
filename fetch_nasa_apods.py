import requests
import os
import json
from dotenv import load_dotenv
from load_helpers import load_image


def fetch_nasa_apod():
    load_dotenv(".env")
    token = os.environ["NASA_API_KEY"]
    params = {
        'api_key': token,
        'start_date': '2026-01-25',
    }
    try:
        response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        params = {
            'api_key': 'DEMO_KEY',
            'start_date': '2026-01-25',
        }
        response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
        response.raise_for_status()
    i = 0
    for image in response.json():
        load_image(image['url'], f'images/nasa_apod_{i}.jpg')
        i += 1


if __name__ == "__main__":
    fetch_nasa_apod()