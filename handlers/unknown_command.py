from aiogram import types, Dispatcher
import message_texts as messages


async def unknown_command(message: types.Message):
    await message.answer(messages.UNKNOWN_COMMAND, parse_mode='HTML')


def register_unknown_command(dp: Dispatcher):
    dp.register_message_handler(unknown_command)
