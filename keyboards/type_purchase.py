from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton("💳 Платное объявление", callback_data='paid_article'),
    InlineKeyboardButton("🔑 Бесплатное объявление", callback_data='free_article'),
]
start_keyboard.add(*buttons)
