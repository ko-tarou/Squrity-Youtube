from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.notice import NoticeCreate, NoticeRead
from crud import notice as crud_notice

router = APIRouter(prefix="/notices", tags=["Notices"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=NoticeRead)
def create_notice_api(notice: NoticeCreate, db: Session = Depends(get_db)):
    return crud_notice.create_notice(db, notice)

@router.get("/{notice_id}", response_model=NoticeRead)
def read_notice_api(notice_id: int, db: Session = Depends(get_db)):
    db_notice = crud_notice.get_notice(db, notice_id)
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    return db_notice
