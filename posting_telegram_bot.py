import telegram
import imghdr
import os
import random
import time
import argparse
from dotenv import load_dotenv
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('hours', nargs='?', default='4')
 
    return parser


def posting_images(interval):
    load_dotenv(".env")
    token = os.environ["POSTING_TELEGRAM_BOT_API_KEY"]
    chat_id = os.environ["TLGRM_CHAT_ID"]
    bot = telegram.Bot(token=token)
    image_names = []
    folder = Path('images')
    for file in folder.iterdir():
    	image_names.append('C:/python_scripts/API_04/images/' + file.name)
    for name in image_names:
        bot.send_photo(chat_id=chat_id, photo=open(name, 'rb'))
        time.sleep(interval)
    while True:
        image_names = random.sample(image_names, len(image_names))
        for name in image_names:
            bot.send_photo(chat_id=chat_id, photo=open(name, 'rb'))
            time.sleep(interval)


if __name__ == "__main__":
    parser = create_parser()
    interval_space = parser.parse_args()
    interval = (3600 * float(interval_space.hours))
    posting_images(interval)

