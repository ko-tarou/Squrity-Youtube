from Alchemy.model import Notice
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Pydantic モデル
class NoticeCreate(BaseModel):
    receive_user_id: int

class NoticeRead(BaseModel):
    notice_id: int
    receive_user_id: int

# DBセッション取得用
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 追加API
@app.post("/notices/", response_model=NoticeRead)
def create_notice(notice: NoticeCreate, db: Session = next(get_db())):
    db_notice = Notice(receive_user_id=notice.receive_user_id)
    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice

# 取得API
@app.get("/notices/{notice_id}", response_model=NoticeRead)
def read_notice(notice_id: int, db: Session = next(get_db())):
    notice = db.query(Notice).filter(Notice.notice_id == notice_id).first()
    if notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    return notice
