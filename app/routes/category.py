from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models.category import Category, CategoryCreate

router = APIRouter()


@router.get("/categories", response_model=list[Category])
async def get_categories():
    return [
        Category(id=1, title="sport"),
        Category(id=2, title="sport")
    ]



@router.post("/categories", response_model=Category)
async def create_category(category: CategoryCreate, session: Session = Depends(get_session)):
    db_category = Category.model_validate(category)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category
