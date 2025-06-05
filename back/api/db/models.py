from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class Notice(Base):
    __tablename__ = "notice"

    notice_id = Column(Integer, primary_key=True, index=True)
    receive_user_id = Column(Integer, nullable=False)