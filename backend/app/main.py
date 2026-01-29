from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.db import engine, Base
from app.api import tasks, webhooks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Task Manager API",
    description = "A simple task manager API",
    version = "1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router)
app.include_router(webhooks.router)