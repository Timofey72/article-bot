from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_confirmation_keyboard(unique_id: str) -> InlineKeyboardMarkup:
    article_confirm_keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("Опубликовать", callback_data=f'publish_{unique_id}'),
        InlineKeyboardButton("Редактировать", callback_data=f'edit_{unique_id}'),
    ]
    article_confirm_keyboard.add(*buttons)
    return article_confirm_keyboard
