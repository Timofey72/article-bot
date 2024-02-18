from typing import List

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

import message_texts as messages
from data.config import bot, BOT_NAME, ADMINS
from keyboards.article_confirmation import get_confirmation_keyboard

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
    if len(description) > 890:
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
    if not price.isdigit() or len(price) > 14:
        await message.answer(messages.PRICE_FORMAT_ERROR)
        return

    await state.update_data(price=price)
    await message.answer(messages.ARTICLE_PHOTO, parse_mode='HTML')
    await ArticleState.photo.set()


async def article_photo(message: types.Message, state: FSMContext, album: List[types.Message] = None):
    photos = []

    if album is None:
        if message.photo:
            photos.append(message.photo[-1].file_id)
            await state.update_data(photos=photos)
            await save_photos(message, state)
            return
        await message.answer(messages.PHOTO_ERROR)
        return

    for i, obj in enumerate(album):
        if obj.photo:
            file_id = obj.photo[-1].file_id
            photos.append(file_id)
    if len(photos) == 0:
        await message.answer(messages.PHOTO_ERROR)
        return

    await state.update_data(photos=photos)
    await save_photos(message, state)


async def save_photos(message: types.Message, state: FSMContext):
    data = await state.get_data()
    description = data.get('description')
    phone = data.get('phone')
    city = data.get('city')
    price = data.get('price')
    photos = data.get('photos')
    check = data.get('check', None)

    article_message = messages.ARTICLE_TEMPLATE % (description, price, city, phone, BOT_NAME)

    if photos is None:
        return

    media_group = []
    for i, photo_id in enumerate(photos):
        media_group.append(
            types.InputMediaPhoto(media=photo_id, parse_mode='HTML', caption=article_message if i == 0 else ''))

    await message.answer(messages.ARTICLE_PHOTO_SAVE)

    user_id = message.from_user.id
    username = message.from_user.username
    article = await article_model.add_article(description, city, phone, price, photos, user_id)
    keyboard = get_confirmation_keyboard(article.id)

    for admin_id in ADMINS:
        await bot.send_media_group(chat_id=int(admin_id), media=media_group)
        if check is not None:
            await bot.send_photo(chat_id=int(admin_id), photo=check, caption=messages.CHECK_TEXT)
        await bot.send_message(chat_id=int(admin_id), text=messages.ARTICLE_PUBLISH % (username, user_id),
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
    dp.register_callback_query_handler(save_photos, state=ArticleState.photo, text='save_photos')
