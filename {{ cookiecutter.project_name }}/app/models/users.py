from sqlalchemy import Column, Integer, String

from app.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
