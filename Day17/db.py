from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Product(Base):
    id = Column(Integer, primary_key=True)
    code = Column(String(20))
    name = Column(String(100))
    price = Column(Integer)
