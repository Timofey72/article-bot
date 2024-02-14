import message_texts as messages


def get_article_message(article: dict) -> tuple:
    description = article.get('description')
    phone = article.get('phone')
    city = article.get('city')
    price = article.get('price')
    return messages.ARTICLE_TEMPLATE % (description, phone, city, price)
