from aiogram.dispatcher.filters.state import StatesGroup, State


class ArticleState(StatesGroup):
    description = State()
    phone = State()
    city = State()
    price = State()
    photo = State()
