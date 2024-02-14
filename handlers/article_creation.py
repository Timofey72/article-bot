from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

import message_texts as messages
from keyboards.payment_confirmation import confirm_keyboard

from state.payment import PaymentState


async def article_info(message: types.Message):
    await message.answer(messages.ARTICLE_INFO, parse_mode='HTML')


def register_article(dp: Dispatcher):
    dp.register_message_handler(article_info, text='free_article')
