from contextlib import asynccontextmanager

from fastapi import FastAPI
from routes import category, post
from database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan,debug=True)
app.include_router(category.router)
app.include_router(post.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications///!"}
