from sqlalchemy import create_engine, Column, Integer, String,Float,ForeignKey
#create engine function from SQLalchemy used to setup the connection to our postgreSQl Db

from sqlalchemy.ext.declarative import declarative_base
#used by sqlalchemy to locate all models and create tables basedon them

from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime
from passlib.context import CryptContext

Base = declarative_base()
pwd_context = CryptContext(schemas=["bcrypt"],deprecated="auto")

class Product(Base):
    __tablename__ = 'products'
    id= Column(Integer,primary_key= True,index=True)
    name = Column(String,index=True)
    description = Column(String)
    price= Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    inventory_count= Column(Integer)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer,primary_key=True,index=True)
    name= Column(String, index=True)
    description= Column(String)
    products= relationship('Product',back_populates='category')

Product.category=relationship('Category', back_populates='products')

class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username= Column(String,unique=True,index=True)
    email= Column(String,unique=True,index=True)
    hashed_password =Column(String)

    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)
    
    def get_password_hash(self, password):
        return pwd_context.hash(password)

class Order(Base):
    __tablename__= 'orders'
    id= Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    status= Column(String)
    created_at = Column(DateTime,default=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = 'order_items'
    id= Column(Integer,primary_key=True,index=True)
    order_id = Column(Integer,ForeignKey('orders.id'))
    Product_id = Column(Integer,ForeignKey('products.id'))
    quantity= Column(Integer)
    price= Column(Float)

