from sqlalchemy import Column, BigInteger, String, sql, Text, ARRAY, Integer

from utils.database.db_gino import BaseModel


class Article(BaseModel):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text)
    city = Column(String(25))
    phone = Column(String(14))
    price = Column(BigInteger)
    photo = Column(ARRAY(String))
    user_id = Column(BigInteger)

    query: sql.Select
