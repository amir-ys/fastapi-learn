from fastapi import FastAPI
from routes import category, post

app = FastAPI()
app.include_router(category.router)
app.include_router(post.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications///!"}
