from sqlalchemy import Column, Integer, String

from app.drivers.database.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), index=True, nullable=False)
    email = Column(String(256), unique=True, index=True)
    hashed_password = Column(String(256), nullable=False)
