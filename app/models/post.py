from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    category_id: int
    is_published: bool


class PostCreate(BaseModel):
    title: str
    content: str
    category_id: int
    is_published: bool