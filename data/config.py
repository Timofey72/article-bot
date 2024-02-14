import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

MODE = str(os.getenv('MODE'))
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
ADMINS = str(os.getenv('ADMINS')).split(',')
MAIN_ADMIN = int(ADMINS[0])
CHANNEL_ID = str(os.getenv('CHANNEL_ID'))

bot = Bot(token=BOT_TOKEN)
