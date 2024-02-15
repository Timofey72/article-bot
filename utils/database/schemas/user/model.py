from sqlalchemy import Column, BigInteger, String, sql

from utils.database.db_gino import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(100))

    query: sql.Select
