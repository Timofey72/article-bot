from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirm_keyboard = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton("✅ Оплатил", callback_data='paid'),
]
confirm_keyboard.add(*buttons)
