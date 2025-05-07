from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Notice(Base):
    __tablename__ = "notice"

    notice_id: int = Column(Integer, primary_key=True, index=True)
    receive_user_id: int = Column(Integer, nullable=False)