from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

photo_keyboard = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton("Добавить фотографию", callback_data='add_photo'),
    InlineKeyboardButton("Сохранить фотографии", callback_data='save_photos'),
]
photo_keyboard.add(*buttons)
