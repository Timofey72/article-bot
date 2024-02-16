from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_keyboard = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton("Список пользователей", callback_data='user_list'),
]
admin_keyboard.add(*buttons)
