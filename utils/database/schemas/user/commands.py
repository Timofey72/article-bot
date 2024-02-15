import logging

from asyncpg import UniqueViolationError

from utils.database.db_gino import db
from utils.database.schemas.user.model import User


async def add_user(user_id: int, username: str):
    user = await select_user(user_id)
    if user is None:
        user = User(id=user_id, username=username)
        await user.create()
    else:
        logging.error(f'UniqueViolationError: id={user_id}; {username=}. User already exists!')

    return user


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(user_id: int):
    user = await User.query.where(User.id == user_id).gino.first()
    return user


async def count_users() -> int:
    total = await db.func.count(User.id).gino.scalar()
    return total
