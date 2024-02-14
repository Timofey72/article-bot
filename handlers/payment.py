from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

import message_texts as messages
from data.config import bot
from handlers.article_creation import start_article_creation
from keyboards.payment_confirmation import confirm_keyboard

from state.payment import PaymentState


async def payment_start(callback_query: types.CallbackQuery):
    await bot.edit_message_text(
        text=messages.PAYMENT_START,
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=confirm_keyboard,
        parse_mode='HTML')
    await PaymentState.start.set()


async def payment_confirmation(callback_query: types.CallbackQuery):
    await bot.edit_message_text(
        messages.PAYMENT_CONFIRM, callback_query.message.chat.id, callback_query.message.message_id)
    await PaymentState.confirm.set()


async def payment_finish(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        await message.answer(messages.PAYMENT_FINISH)
        await state.finish()
        await start_article_creation(message, message.photo[-1].file_id)
    else:
        await message.answer(messages.NOT_CORRECT_CHECK)


def register_payment(dp: Dispatcher):
    dp.register_callback_query_handler(payment_start, text='paid_article')
    dp.register_callback_query_handler(payment_confirmation, text='paid', state=PaymentState.start)
    dp.register_message_handler(payment_finish, content_types=ContentType.ANY, state=PaymentState.confirm)
