from aiogram import Dispatcher, types
from data.config import bot, CHANNEL_ID
from utils.article_dict import get_article_message

from utils.articles_json import find_article_by_id_in_json, delete_article_by_id


async def publish_article(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    article_id = callback_query.data.replace('publish_', '')
    article = find_article_by_id_in_json(article_id)
    delete_article_by_id(article_id)

    if article is None:
        await callback_query.answer('Произошла ошибка при публикации')
        return

    photos = article.get('photos')
    article_message = get_article_message(article)

    media_group = []
    for i, photo_id in enumerate(photos):
        media_group.append(
            types.InputMediaPhoto(media=photo_id, parse_mode='HTML', caption=article_message if i == 0 else ''))

    await bot.send_media_group(chat_id=CHANNEL_ID, media=media_group)
    await callback_query.answer('Статья опубликована')


def register_confirmation_article(dp: Dispatcher):
    dp.register_callback_query_handler(publish_article, lambda c: c.data.startswith('publish_'))
