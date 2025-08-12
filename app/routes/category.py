from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CategoryCreate(BaseModel):
    name: str

@router.post("/categories/")
async def create_category(category: CategoryCreate):
    return {"message": f"Kategori '{category.name}' berhasil dibuat"}
