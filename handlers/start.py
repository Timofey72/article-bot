from aiogram import Dispatcher, types
import message_texts as messages

from keyboards.type_purchase import start_keyboard


async def start(message: types.Message):
    await message.answer(messages.START, reply_markup=start_keyboard)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
