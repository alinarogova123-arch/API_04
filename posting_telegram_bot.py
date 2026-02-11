import telegram
import imghdr
import os
import random
import time
import argparse
from dotenv import load_dotenv
from pathlib import Path
from load_helpers import decrease_image


def create_parser():
    parser = argparse.ArgumentParser(description="Запускает telegram бота по загрузке фотографий с нужным интервалом")
    parser.add_argument('hours', nargs='?', default='4', type=str, help="Интервал между загрузками фотографий в часах")
 
    return parser


def launch_upload_bot(interval, token, chat_id):
    bot = telegram.Bot(token=token)
    absolute_path = Path('images').resolve()
    image_names = []
    folder = Path('images')
    for file in folder.iterdir():
    	image_names.append(absolute_path / file.name)
    while True:
        for name in image_names:
            name = decrease_image(name)
            with open(name, 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(interval)
        image_names = random.sample(image_names, len(image_names))


if __name__ == "__main__":
    load_dotenv(".env")
    token = os.environ["POSTING_TELEGRAM_BOT_API_KEY"]
    chat_id = os.environ["TLGRM_CHAT_ID"]
    parser = create_parser()
    interval_space = parser.parse_args()
    interval = (3600 * float(interval_space.hours))
    launch_upload_bot(interval, token, chat_id)

