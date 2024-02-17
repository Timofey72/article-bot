from aiogram import Dispatcher, types

from data.config import bot, CHANNEL_ID, BOT_NAME
import message_texts as messages
from keyboards.article_confirmation import get_edit_article_keyboard

from utils.database.schemas.article import commands as article_model


async def publish_article(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    article_id = int(callback_query.data.replace('publish_', ''))
    article = await article_model.select_article(article_id)

    if article is None:
        await callback_query.answer('Произошла ошибка при публикации')
        return

    photos = article.photo
    article_message = messages.ARTICLE_TEMPLATE % (
        article.description, article.price, article.city, article.phone, BOT_NAME)

    media_group = []
    for i, photo_id in enumerate(photos):
        media_group.append(
            types.InputMediaPhoto(media=photo_id, parse_mode='HTML', caption=article_message if i == 0 else ''))

    await bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
    await callback_query.answer('Статья опубликована')


async def edit_article(callback_query: types.CallbackQuery):
    article_id = int(callback_query.data.replace('edit_', ''))
    keyboard = get_edit_article_keyboard(article_id)
    await bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                        reply_markup=keyboard)


def register_confirmation_article(dp: Dispatcher):
    dp.register_callback_query_handler(publish_article, lambda c: c.data.startswith('publish_'))
    dp.register_callback_query_handler(edit_article, lambda c: c.data.startswith('edit_'))
