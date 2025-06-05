from fastapi import FastAPI
from api import notice

app = FastAPI()

app.include_router(notice.router)
