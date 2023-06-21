from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from db import Base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

    

   
    
