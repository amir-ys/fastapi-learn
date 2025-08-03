from fastapi import APIRouter
from models.category import Category,CategoryCreate

router = APIRouter()


@router.get("/categories", response_model=list[Category])
async def get_categories():
    return [
        Category(id=1, title="sport"),
        Category(id=2, title="sport")
    ]

@router.post("/categories")
async def create_category(category: CategoryCreate):
    category  =  Category(id=1,title=category.title , description=category.description)

    return category
