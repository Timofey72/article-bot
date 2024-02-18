import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

MODE = str(os.getenv('MODE'))
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
ADMINS = str(os.getenv('ADMINS')).split(',')
CHANNEL_ID = str(os.getenv('CHANNEL_ID'))
BOT_NAME = str(os.getenv('BOT_NAME'))

PG_NAME = str(os.getenv('PG_NAME'))
PG_USER = str(os.getenv('PG_USER'))
PG_PASS = str(os.getenv('PG_PASS'))
PG_HOST = str(os.getenv('PG_HOST'))

CARD = str(os.getenv('CARD'))
PRICE = str(os.getenv('PRICE'))
BANK = str(os.getenv('BANK'))
ADMIN_URL = str(os.getenv('ADMIN_URL'))

POSTGRES_URI = f'postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}/{PG_NAME}'

bot = Bot(token=BOT_TOKEN)
