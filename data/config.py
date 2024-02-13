import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

MODE = str(os.getenv('MODE'))
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
ADMINS = str(os.getenv('ADMINS')).split(',')

bot = Bot(token=BOT_TOKEN)
