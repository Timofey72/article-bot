from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

import message_texts as messages

from keyboards.type_purchase import start_keyboard


async def start(message: types.Message, state: FSMContext):
    # clearing all states
    await state.finish()
    await message.answer(messages.START, reply_markup=start_keyboard)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state='*')
