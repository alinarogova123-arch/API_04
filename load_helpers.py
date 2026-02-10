import requests
import os
import json
from PIL import Image


def decrease_image(path):
    image = Image.open(path)
    image.thumbnail((2000, 1400))
    image.save(path)

    return path


def load_image(url, path):
    os.makedirs("images", exist_ok=True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
