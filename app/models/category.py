from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class BaseCategory(SQLModel):
    title: str
    description: Optional[str] = None


class CategoryCreate(BaseCategory):
    pass

class Category(BaseCategory , table=True):
    id: Optional[int] = Field(None, primary_key=True)
