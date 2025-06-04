from sqlalchemy import Column, Integer, String, Boolean
from da.database import Base


class Notice(Base):
    __tablename__ = "notice"

    notice_id = Column(Integer, primary_key=True, index=True)
    receive_user_id = Column(Integer, nullable=False)

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)