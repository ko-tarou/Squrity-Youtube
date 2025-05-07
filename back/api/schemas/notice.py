from pydantic import BaseModel

class NoticeCreate(BaseModel):
    receive_user_id: int

class NoticeRead(BaseModel):
    notice_id: int
    receive_user_id: int