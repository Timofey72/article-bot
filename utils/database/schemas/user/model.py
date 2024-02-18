from sqlalchemy import Column, BigInteger, String, sql, Boolean

from utils.database.db_gino import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(100))
    is_blocked = Column(Boolean, unique=False, default=False)

    query: sql.Select
