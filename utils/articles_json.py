import json
import os
from typing import Optional

path_to_file = 'articles.json'


def is_file_exists_or_empty(path: str) -> bool:
    """Checks a file for existence and size. Return True if exists"""
    return os.path.exists(path) and os.path.getsize(path) > 0


def save_article_to_json(unique_id: str, article_data: dict) -> None:
    if is_file_exists_or_empty(path_to_file):
        with open(path_to_file, 'r') as f:
            articles_list = json.load(f)
    else:
        articles_list = []

    articles_list.append({unique_id: article_data})

    with open(path_to_file, 'w') as f:
        json.dump(articles_list, f, indent=2)


def find_article_by_id_in_json(article_id) -> Optional[dict]:
    if is_file_exists_or_empty(path_to_file):
        with open(path_to_file, 'r') as f:
            articles_list = json.load(f)

        for article in articles_list:
            _article = article.get(article_id)
            if _article:
                return _article
    return None


def delete_article_by_id(article_id) -> bool:
    if is_file_exists_or_empty(path_to_file):
        with open(path_to_file, 'r') as f:
            articles_list = json.load(f)

        for article in articles_list:
            if article.get(article_id):
                articles_list.remove(article)
                with open('articles.json', 'w') as f:
                    json.dump(articles_list, f, ensure_ascii=False, indent=4)
                return True

    return False
