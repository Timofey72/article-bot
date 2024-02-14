from aiogram import Dispatcher, types

import message_texts as messages
from data.config import bot
from handlers.article_creation import start_article_creation


async def free_info(callback_query: types.CallbackQuery):
    await bot.edit_message_text(
        text=messages.ARTICLE_FREE_INFO,
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )
    await start_article_creation(callback_query.message)


def register_free_article(dp: Dispatcher):
    dp.register_callback_query_handler(free_info, text='free_article')
