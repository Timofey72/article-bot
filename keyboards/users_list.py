from math import ceil

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.database.schemas.user import commands as user_model


async def get_users_pagination_keyboard(current_page: int = 1, offset: int = 4):
    users = await user_model.select_all_users()
    users_list = [user for user in users]

    total_pages = ceil(len(users_list) / offset)

    if current_page < 1:
        current_page = total_pages
    if current_page > total_pages:
        current_page = 1

    start_index = (current_page - 1) * offset
    end_index = start_index + offset
    visible_list = users_list[start_index: end_index]

    chunks = [visible_list[i: i + 1] for i in range(0, len(visible_list))]
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(InlineKeyboardButton("📢 Отправить всем", callback_data='send_for_all'))

    for row in chunks:
        buttons = [
            InlineKeyboardButton(text=f'@{user.username}. ID: {user.id}', callback_data=f'send_for_{user.id}')
            for user in row]
        markup.add(*buttons)

    pagination_buttons = [
        InlineKeyboardButton("<-", callback_data=f'prev_page_{current_page}'),
        InlineKeyboardButton(f'{current_page}/{total_pages}', callback_data=f'current_page_{current_page}'),
        InlineKeyboardButton("->", callback_data=f'next_page_{current_page}')
    ]

    markup.add(*pagination_buttons)
    markup.add(InlineKeyboardButton("↩️ Назад", callback_data='admin_back'))

    return markup
