import logging

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import bot
from handlers import start, payment, article_creation, free, admin, confirmation, edit_article

from utils.database import db_gino

dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(dispatcher):
    start.register_start(dispatcher)
    admin.register_admin(dispatcher)
    payment.register_payment(dispatcher)
    article_creation.register_article(dispatcher)
    free.register_free_article(dispatcher)
    edit_article.register_edit_article(dispatcher)
    confirmation.register_confirmation_article(dispatcher)

    logging.info('Database starting')
    await db_gino.on_startup()
    await db_gino.db.gino.create_all()
    logging.info('Database started')

    logging.info('Bot started')
