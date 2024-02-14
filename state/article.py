from aiogram.dispatcher.filters.state import StatesGroup, State


class ArticleState(StatesGroup):
    description = State()
    city = State()
    phone = State()
    price = State()
    photo = State()
