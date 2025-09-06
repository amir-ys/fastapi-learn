from contextlib import asynccontextmanager

from fastapi import FastAPI
from database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan,debug=True)

@app.get("/ping")
async def root():
    return {"message": "pong"}
