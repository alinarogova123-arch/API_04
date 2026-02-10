import requests
import json
import argparse
from load_helpers import load_image


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_number', nargs='?', default='100')
 
    return parser


def fetch_spacex_launch(launch):
    response = requests.get(f"https://api.spacexdata.com/v3/launches/{launch}")
    response.raise_for_status()   
    for image_number, image in enumerate(response.json()['links']['flickr_images']):
        load_image(image, f'images/spacex_{image_number}.jpg')
        

if __name__ == "__main__":
    parser = create_parser()
    launch_space = parser.parse_args()
    launch = launch_space.launch_number
    try:
        fetch_spacex_launch(launch)
    except requests.exceptions.HTTPError:
        print("Выберите номер запуска до 100")
