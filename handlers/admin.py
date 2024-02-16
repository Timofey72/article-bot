from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

import message_texts as messages

from data.config import ADMINS, bot
from handlers.unknown_command import unknown_command
from keyboards.users_list import get_users_pagination_keyboard
from keyboards.admin import admin_keyboard


async def admin_start(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    if user_id not in ADMINS:
        await unknown_command(message)
        return

    # clearing all states
    await state.finish()

    await message.answer(messages.ADMIN_GREETING, parse_mode='HTML', reply_markup=admin_keyboard)


async def user_list(callback_query: types.CallbackQuery, current_page: int = 1):
    await callback_query.answer(cache_time=1)
    keyboard = await get_users_pagination_keyboard(current_page=current_page)
    await bot.edit_message_text(text=messages.ADMIN_SEND_MESSAGE,
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=keyboard)


async def back(callback_query: types.CallbackQuery):
    await callback_query.answer(cache_time=3)
    await bot.edit_message_text(text=messages.ADMIN_GREETING,
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                parse_mode='HTML',
                                reply_markup=admin_keyboard)


async def pagination_next_page(callback_query: types.CallbackQuery):
    next_page = int(callback_query.data.replace('next_page_', '')) + 1
    await user_list(callback_query, current_page=next_page)


async def pagination_prev_page(callback_query: types.CallbackQuery):
    prev_page = int(callback_query.data.replace('prev_page_', '')) - 1
    await user_list(callback_query, current_page=prev_page)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'], state='*')
    dp.register_callback_query_handler(user_list, text='user_list')
    dp.register_callback_query_handler(pagination_next_page, lambda c: c.data.startswith('next_page_'))
    dp.register_callback_query_handler(pagination_prev_page, lambda c: c.data.startswith('prev_page_'))
    dp.register_callback_query_handler(back, text='admin_back')
