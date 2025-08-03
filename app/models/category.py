from typing import Optional
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    title: str
    description: Optional[str] = None


class CategoryCreate(BaseModel):
    title: str
    description: Optional[str] = None