from typing import Optional
from pydantic import BaseModel

# ----------------------
# User Schemas
# ----------------------
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Fix untuk Pydantic v2


# ----------------------
# Task Schemas
# ----------------------
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TaskResponse(TaskBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  # Fix untuk Pydantic v2

# ----------------------
# Category Schemas
# ----------------------
class CategoryCreate(BaseModel):
    name: str
    