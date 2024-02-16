from typing import Union

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

import message_texts as messages
from data.config import bot, MAIN_ADMIN
from keyboards.article_confirmation import get_confirmation_keyboard
from keyboards.photo import photo_keyboard

from state.article import ArticleState
from utils.database.schemas.article import commands as article_model

check_image_id: str = ''


async def start_article_creation(message: types.Message, check: str = None):
    global check_image_id
    await message.answer(messages.ARTICLE_DESCRIPTION, parse_mode='HTML')
    await ArticleState.description.set()
    check_image_id = check


async def article_description(message: types.Message, state: FSMContext):
    global check_image_id
    if check_image_id:
        await state.update_data(check=check_image_id)
        check_image_id = ''

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
    if len(phone) > 14 or not phone.startswith('+7') or not phone.replace('+7', '').isdigit():
        await message.answer(messages.PHONE_FORMAT_ERROR)
        return

    await state.update_data(phone=phone)
    await message.answer(messages.ARTICLE_PRICE, parse_mode='HTML')
    await ArticleState.price.set()


async def article_price(message: types.Message, state: FSMContext):
    price = message.text
    if not price.isdigit() or len(price) > 6:
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

    if len(data['photos']) == 10:
        await save_photos(message, state)
        return

    await message.answer(messages.ARTICLE_PHOTO_SUCCESS, reply_markup=photo_keyboard, parse_mode='HTML')


async def add_photo(callback_query: types.CallbackQuery):
    await callback_query.message.answer(messages.ARTICLE_PHOTO, parse_mode='HTML')
    await ArticleState.photo.set()


async def save_photos(action_type: Union[types.CallbackQuery, types.Message], state: FSMContext):
    data = await state.get_data()
    description = data.get('description')
    phone = data.get('phone')
    city = data.get('city')
    price = data.get('price')
    photos = data.get('photos')
    check = data.get('check', None)

    article_message = messages.ARTICLE_TEMPLATE % (description, phone, city, price)

    if photos is None:
        return

    media_group = []
    for i, photo_id in enumerate(photos):
        media_group.append(
            types.InputMediaPhoto(media=photo_id, parse_mode='HTML', caption=article_message if i == 0 else ''))

    if type(action_type) is types.Message:
        await action_type.answer(messages.ARTICLE_PHOTO_SAVE)
    else:
        await action_type.message.answer(messages.ARTICLE_PHOTO_SAVE)

    user_id = action_type.from_user.id
    username = action_type.from_user.username
    article = await article_model.add_article(description, city, phone, price, photos, user_id)
    keyboard = get_confirmation_keyboard(article.id)

    await bot.send_media_group(chat_id=MAIN_ADMIN, media=media_group)
    if check is not None:
        await bot.send_photo(chat_id=MAIN_ADMIN, photo=check, caption=messages.CHECK_TEXT)
    await bot.send_message(chat_id=MAIN_ADMIN, text=messages.ARTICLE_PUBLISH % (username, user_id),
                           reply_markup=keyboard,
                           parse_mode='HTML')

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
