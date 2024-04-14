import asyncio
from typing import Union

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.database.schemas.user import commands as user_model


class AlbumMiddleware(BaseMiddleware):
    """This middleware is for capturing media groups."""

    album_data: dict = {}

    def __init__(self, latency: Union[int, float] = 0.1):
        """
        You can provide custom latency to make sure
        albums are handled properly in highload.
        """
        self.latency = latency
        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        if not message.media_group_id:
            return

        try:
            self.album_data[message.media_group_id].append(message)
            raise CancelHandler()  # Tell aiogram to cancel handler for this group element
        except KeyError:
            self.album_data[message.media_group_id] = [message]
            await asyncio.sleep(self.latency)

            message.conf["is_last"] = True
            data["album"] = self.album_data[message.media_group_id]

    async def on_post_process_message(self, message: types.Message, result: dict, data: dict):
        """Clean up after handling our album."""
        if message.media_group_id and message.conf.get("is_last"):
            del self.album_data[message.media_group_id]


class UserBannedMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        user = await user_model.select_user(message.from_user.id)
        if user and user.is_blocked:
            await message.answer(
                '<b>Ваш аккаунт заблокирован!</b>',
                parse_mode='HTML'
            )
            raise CancelHandler

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        user = await user_model.select_user(callback_query.from_user.id)
        if user and user.is_blocked:
            await callback_query.answer(
                'Ваш аккаунт заблокирован!',
                show_alert=True
            )
            raise CancelHandler

    async def on_process_inline_query(self, query: types.InlineQuery, data: dict):
        user = await user_model.select_user(query.from_user.id)
        if user and user.is_blocked:
            raise CancelHandler
