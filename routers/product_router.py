from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from database import get_db
from models import Product
from schemas import ProductCreate,Product as ProductSchema

router = APIRouter()

@router.post("/products/", response_model=ProductSchema)
async def create_product(product: ProductCreate,db: AsyncSession= Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

@router.get("/products/", response_model=List[ProductSchema])
async def read_products(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Product))
        products = result.scalars().all()
        return products

@router.get("/products/{product_id}", response_model=ProductSchema)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=ProductSchema)
async def update_product(product_id: int, product: ProductCreate, db: AsyncSession = Depends(get_db)):
    existing_product = await db.get(Product, product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for var, value in vars(product).items():
        setattr(existing_product, var, value) if value else None
    db.add(existing_product)
    await db.commit()
    return existing_product

@router.delete("/products/{product_id}", response_model=ProductSchema)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    await db.delete(product)
    await db.commit()
    return product
