from typing import Union

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

import message_texts as messages
from data.config import bot
from keyboards.photo import photo_keyboard

from state.article import ArticleState


async def start_article_creation(message: types.Message):
    await message.answer(messages.ARTICLE_DESCRIPTION, parse_mode='HTML')
    await ArticleState.description.set()


async def article_description(message: types.Message, state: FSMContext):
    description = message.text
    if len(description) > 900:
        await message.answer(messages.DESCRIPTION_LIMIT)
        return

    await state.update_data(description=description)
    await message.answer(messages.ARTICLE_CITY, parse_mode='HTML')
    await ArticleState.city.set()


async def article_city(message: types.Message, state: FSMContext):
    city = message.text
    if len(city) > 25:
        await message.answer(messages.CITY_LIMIT)
        return

    await state.update_data(city=city)
    await message.answer(messages.ARTICLE_PHONE, parse_mode='HTML')
    await ArticleState.phone.set()


async def article_phone(message: types.Message, state: FSMContext):
    phone = message.text
    if len(phone) > 14 or not phone.startswith('+7'):
        await message.answer(messages.PHONE_FORMAT_ERROR)
        return

    await state.update_data(phone=phone)
    await message.answer(messages.ARTICLE_PRICE, parse_mode='HTML')
    await ArticleState.price.set()


async def article_price(message: types.Message, state: FSMContext):
    price = message.text
    if not price.isdigit():
        await message.answer(messages.PRICE_FORMAT_ERROR)
        return

    await state.update_data(price=price)
    await message.answer(messages.ARTICLE_PHOTO, parse_mode='HTML')
    await ArticleState.photo.set()


async def article_photo(message: types.Message, state: FSMContext):
    photo = message.photo

    if not photo:
        await message.answer(messages.PHOTO_ERROR)
        return

    photo = photo[-1]

    async with state.proxy() as data:
        if 'photos' not in data:
            data['photos'] = [photo.file_id]
        else:
            data['photos'].append(photo.file_id)

    if len(data['photos']) == 3:
        await save_photos(message, state)
        return

    await message.answer(messages.ARTICLE_PHOTO_SUCCESS, reply_markup=photo_keyboard, parse_mode='HTML')


async def add_photo(callback_query: types.CallbackQuery):
    await callback_query.message.answer(messages.ARTICLE_PHOTO, parse_mode='HTML')
    await ArticleState.photo.set()


async def save_photos(action_type: Union[types.CallbackQuery, types.Message], state: FSMContext):
    data = await state.get_data()

    if type(action_type) is types.Message:
        await action_type.answer(messages.ARTICLE_PHOTO_SAVE)
    else:
        await action_type.message.answer(messages.ARTICLE_PHOTO_SAVE)

    await state.finish()


def register_article(dp: Dispatcher):
    dp.register_message_handler(start_article_creation, text='free_article')
    dp.register_message_handler(article_description, state=ArticleState.description)
    dp.register_message_handler(article_city, state=ArticleState.city)
    dp.register_message_handler(article_phone, state=ArticleState.phone)
    dp.register_message_handler(article_price, state=ArticleState.price)
    dp.register_message_handler(article_photo, content_types=ContentType.ANY, state=ArticleState.photo)
    dp.register_callback_query_handler(add_photo, state=ArticleState.photo, text='add_photo')
    dp.register_callback_query_handler(save_photos, state=ArticleState.photo, text='save_photos')
