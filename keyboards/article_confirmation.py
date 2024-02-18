from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_confirmation_keyboard(article_id: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("Опубликовать", callback_data=f'publish_{article_id}'),
        InlineKeyboardButton("Редактировать", callback_data=f'edit_{article_id}'),
        InlineKeyboardButton("Заблокировать пользователя", callback_data=f'block_user_{article_id}'),
    ]
    keyboard.add(*buttons)
    return keyboard


def get_edit_article_keyboard(article_id: int):
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("Изменить описание", callback_data=f'edit_description_{article_id}'),
        InlineKeyboardButton("Изменить город", callback_data=f'edit_city_{article_id}'),
        InlineKeyboardButton("Изменить номер", callback_data=f'edit_phone_{article_id}'),
        InlineKeyboardButton("Изменить цену", callback_data=f'edit_price_{article_id}'),
        InlineKeyboardButton("↩️ Назад", callback_data=f'edit_back_{article_id}'),
    ]
    keyboard.add(*buttons)
    return keyboard
