from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine
from models import Base
from routers import product_router,category_router
from dotenv import load_dotenv
import os

# load environment variables from .env file if present
load_dotenv()

# get the secret key from snvironment vairables or use a default if not found
SECRET_KEY = os.getenv('SECRET_KEY')

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Application startup: Database tables created.")
    
    yield  # Control is given to the app here
    
    # Shutdown logic
    print("Application shutdown: Clean up actions can be performed here.")

app = FastAPI(lifespan=lifespan)

# Include your product router for product-related endpoints and category too
app.include_router(product_router.router)
app.include_router(category_router.router)
