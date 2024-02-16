import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked

import message_texts as messages

from data.config import bot
from utils.database.schemas.user import commands as user_model


async def send_for_all(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_text(text=messages.MESSAGE_FOR_ALL,
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id)
    await state.set_state('message_all')


async def message_for_all(message: types.Message, state: FSMContext):
    text = message.text
    users = await user_model.select_all_users()
    users_ids = [user.id for user in users]

    await message.answer(messages.MESSAGE_SENT_SUCCESS)
    await state.finish()

    for user_id in users_ids:
        try:
            await bot.send_message(chat_id=user_id, text=text)
        except Exception:
            logging.error('Bot was blocked by the user %s' % user_id)


async def send_for_user(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = int(callback_query.data.replace('send_for_', ''))
    await bot.edit_message_text(text=messages.MESSAGE_FOR_USER % user_id,
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                parse_mode='HTML')
    await state.set_state('message_user')
    await state.update_data(user_id=user_id)


async def message_for_user(message: types.Message, state: FSMContext):
    user_id = (await state.get_data()).get('user_id')
    text = message.text

    await message.answer(messages.MESSAGE_SENT_SUCCESS)
    await state.finish()
    try:
        await bot.send_message(text=text, chat_id=user_id)
    except Exception:
        logging.error('Bot was blocked by the user %s' % user_id)


def register_newsletter(dp: Dispatcher):
    dp.register_callback_query_handler(send_for_all, text='send_for_all')
    dp.register_callback_query_handler(send_for_user, lambda c: c.data.startswith('send_for_'))
    dp.register_message_handler(message_for_all, state='message_all')
    dp.register_message_handler(message_for_user, state='message_user')
