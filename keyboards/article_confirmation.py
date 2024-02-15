from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_confirmation_keyboard(article_id: str) -> InlineKeyboardMarkup:
    article_confirm_keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("Опубликовать", callback_data=f'publish_{article_id}'),
        InlineKeyboardButton("Редактировать", callback_data=f'edit_{article_id}'),
    ]
    article_confirm_keyboard.add(*buttons)
    return article_confirm_keyboard
