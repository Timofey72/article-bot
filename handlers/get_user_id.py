from aiogram import types, Dispatcher


async def get_user_id(message: types.Message):
    user_id = message.from_user.id
    await message.answer(text=f'<code>{user_id}</code>', parse_mode='HTML')


def register_get_user_id(dp: Dispatcher):
    dp.register_message_handler(get_user_id, commands=['my_id'])
