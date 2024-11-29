from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/e-comm-fastapi"
engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = sessionmaker(autocommit= False,autoflush = False,bind= engine,class_=AsyncSession)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session