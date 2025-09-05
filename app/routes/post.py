from fastapi import APIRouter
from models.post import PostCreate, Post

router = APIRouter()


@router.post("/posts", response_model=Post)
async def create_post(post: PostCreate):
    post = Post(
        id=1,
        title=post.title,
        content=post.content,
        category_id=post.category_id,
        is_published=post.is_published
    )
    return post
