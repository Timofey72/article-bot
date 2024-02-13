import logging

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import bot
from handlers import start, payment

dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(dispatcher):
    start.register_start(dispatcher)
    payment.register_payment(dispatcher)

    logging.info('Bot started')
