from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from data.config import bot
import message_texts as messages
from keyboards.article_confirmation import get_confirmation_keyboard
from utils.database.schemas.article import commands as article_model


async def edit_description(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=5)
    article_id = int(callback_query.data.replace('edit_description_', ''))
    await callback_query.message.answer(messages.EDIT_DESCRIPTION)
    await state.set_state('edit')
    await state.update_data(article_id=article_id, type='description')


async def edit_city(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=5)
    article_id = int(callback_query.data.replace('edit_city_', ''))
    await callback_query.message.answer(messages.EDIT_CITY)
    await state.set_state('edit')
    await state.update_data(article_id=article_id, type='city')


async def edit_phone(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=5)
    article_id = int(callback_query.data.replace('edit_phone_', ''))
    await callback_query.message.answer(messages.EDIT_PHONE)
    await state.set_state('edit')
    await state.update_data(article_id=article_id, type='phone')


async def edit_price(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=5)
    article_id = int(callback_query.data.replace('edit_price_', ''))
    await callback_query.message.answer(messages.EDIT_PRICE)
    await state.set_state('edit')
    await state.update_data(article_id=article_id, type='price')


async def edit_article_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    article_id = int(data.get('article_id'))
    edit_type = data.get('type')

    text = message.text

    if edit_type == 'description':
        if len(text) > 890:
            await message.answer(messages.DESCRIPTION_LIMIT)
            return
        await article_model.update_article(article_id=article_id, description=text)
    elif edit_type == 'city':
        if len(text) > 25:
            await message.answer(messages.CITY_LIMIT)
            return
        await article_model.update_article(article_id=article_id, city=text)
    elif edit_type == 'phone':
        if len(text) > 14 or not text.startswith('+7') or not text.replace('+7', '').isdigit():
            await message.answer(messages.PHONE_FORMAT_ERROR)
            return
        await article_model.update_article(article_id=article_id, phone=text)
    elif edit_type == 'price':
        if not text.isdigit() or len(text) > 14:
            await message.answer(messages.PRICE_FORMAT_ERROR)
            return
        await article_model.update_article(article_id=article_id, price=text)

    await message.answer(messages.EDIT_SUCCESS)
    await state.finish()


async def edit_back(callback_query: types.CallbackQuery):
    article_id = int(callback_query.data.replace('edit_back_', ''))
    keyboard = get_confirmation_keyboard(article_id)
    await bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                        reply_markup=keyboard)


def register_edit_article(dp: Dispatcher):
    dp.register_callback_query_handler(edit_description, lambda c: c.data.startswith('edit_description_'))
    dp.register_callback_query_handler(edit_city, lambda c: c.data.startswith('edit_city_'))
    dp.register_callback_query_handler(edit_phone, lambda c: c.data.startswith('edit_phone_'))
    dp.register_callback_query_handler(edit_price, lambda c: c.data.startswith('edit_price_'))
    dp.register_message_handler(edit_article_data, state='edit')
    dp.register_callback_query_handler(edit_back, lambda c: c.data.startswith('edit_back_'))
