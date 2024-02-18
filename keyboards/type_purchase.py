from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import ADMIN_URL

start_keyboard = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton("Реклама", url=ADMIN_URL),
    InlineKeyboardButton("Публикация без очереди", callback_data='paid_article'),
    InlineKeyboardButton("Бесплатная публикация", callback_data='free_article'),
]
start_keyboard.add(*buttons)
