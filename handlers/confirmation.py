from aiogram import Dispatcher, types
from data.config import bot, CHANNEL_ID
import message_texts as messages

from utils.database.schemas.article import commands as article_model


async def publish_article(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    article_id = int(callback_query.data.replace('publish_', ''))
    article = await article_model.select_article(article_id)

    if article is None:
        await callback_query.answer('Произошла ошибка при публикации')
        return

    photos = article.photo
    article_message = messages.ARTICLE_TEMPLATE % (article.description, article.phone, article.city, article.price)

    media_group = []
    for i, photo_id in enumerate(photos):
        media_group.append(
            types.InputMediaPhoto(media=photo_id, parse_mode='HTML', caption=article_message if i == 0 else ''))

    await bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
    await callback_query.answer('Статья опубликована')


def register_confirmation_article(dp: Dispatcher):
    dp.register_callback_query_handler(publish_article, lambda c: c.data.startswith('publish_'))
