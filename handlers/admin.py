from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

import message_texts as messages

from data.config import MAIN_ADMIN


async def admin_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id != MAIN_ADMIN:
        return

    # clearing all states
    await state.finish()

    await message.answer(messages.ADMIN_GREETING % user_id, parse_mode='HTML')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'], state='*')
