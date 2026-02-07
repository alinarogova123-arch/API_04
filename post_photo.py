import telegram
import imghdr
import os
import random
import argparse
from dotenv import load_dotenv
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?', default=None)
 
    return parser


def posting_image(photo_name):
    load_dotenv(".env")
    token = os.environ["POSTING_TELEGRAM_BOT_API_KEY"]
    chat_id = os.environ["TLGRM_CHAT_ID"]
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id, photo=open(photo_name, 'rb'))


if __name__ == "__main__":
    image_names = []
    folder = Path('images')
    for file in folder.iterdir():
        image_names.append('C:/python_scripts/API_04/images/' + file.name)
    parser = create_parser()
    name_space = parser.parse_args()
    if name_space.name:
        photo_name = ('C:/python_scripts/API_04/images/' + name_space.name)
    else:
        photo_name = random.choice(image_names)
    try:
        posting_image(photo_name)
    except FileNotFoundError:
            print("Не правильное имя файла")
