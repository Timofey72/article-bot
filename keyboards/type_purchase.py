from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton("Реклама", url='https://t.me/agent_tg1'),
    InlineKeyboardButton("Публикация без очереди", callback_data='paid_article'),
    InlineKeyboardButton("Бесплатная публикация", callback_data='free_article'),
]
start_keyboard.add(*buttons)
