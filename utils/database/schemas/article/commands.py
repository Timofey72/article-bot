from typing import List

from utils.database.schemas.article.model import Article


async def add_article(description: str, city: str, phone: str, price: int, photo: List[str], user_id: str):
    article = Article(description=description, city=city, phone=phone, price=int(price), photo=photo, user_id=user_id)
    await article.create()
    return article


async def select_article(article_id: int):
    user = await Article.query.where(Article.id == article_id).gino.first()
    return user


async def update_article(
        article_id: int, *, description: str = None, city: str = None, phone: str = None, price: int = None):
    article = await Article.get(id=article_id)
    if description:
        await article.update(description=description)
    if city:
        await article.update(city=city)
    if phone:
        await article.update(phone=phone)
    if price:
        await article.update(price=int(price))
