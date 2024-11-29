# schemas.py provides schemas for data validation ands serilization using pydantic

from pydantic import BaseModel

class ProductBase(BaseModel):
    name : str
    description  : str = None
    price : float
    category_id : int
    inventory_count : int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id : int

    class config:
        orm_mode = True

class CategoryBase(BaseModel):
    name : str
    description : str = None

class CategoryCreate(CategoryBase):
    pass
class Category(CategoryBase):
    id : int

    class config:
        orm_mode = True


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserInBD(UserBase):
    id: int
    hashed_password: str
class User(UserBase):
    id: int