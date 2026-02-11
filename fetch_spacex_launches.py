import requests
import json
import argparse
from load_helpers import load_image


def create_parser():
    parser = argparse.ArgumentParser(description="Скачивает фотографии запуска ракет SpaceX")
    parser.add_argument('launch_number', nargs='?', default='100', type=int, help="Номер запуска ракеты SpaceX")
 
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
    fetch_spacex_launch(launch)




