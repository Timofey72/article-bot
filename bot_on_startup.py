import logging

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import bot
from handlers import start, payment, article_creation, free, admin, confirmation

dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(dispatcher):
    start.register_start(dispatcher)
    admin.register_admin(dispatcher)
    payment.register_payment(dispatcher)
    article_creation.register_article(dispatcher)
    free.register_free_article(dispatcher)
    confirmation.register_confirmation_article(dispatcher)

    logging.info('Bot started')
