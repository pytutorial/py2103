from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from urllib.parse import quote
Base = declarative_base()

db_host = '34.122.175.106'       #/phpmyadmin
db_user = 'test'                 # localhost (admin)
db_pass = quote('abc@123')       # abc%40123
db_name = 'py2103'  # tao rieng
conn_url= f'mysql://{db_user}:{db_pass}@{db_host}/{db_name}?charset=utf8'

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    code = Column(String(30), unique=True)
    name = Column(String(200))
    price = Column(Integer)

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    phone = Column(String(20), unique=True)
    address = Column(String(200))

class Order(Base):
    __tablename__ = 'pos_order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer')
    date = Column(DateTime)

class OrderItem(Base):
    __tablename__ = 'pos_order_item'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('pos_order.id')) 
    order = relationship('Order')
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product')
    qty = Column(Integer)
    price_unit = Column(Integer)

engine = create_engine(conn_url)
Session = sessionmaker(bind=engine)
if __name__ == '__main__':
    Base.metadata.create_all(engine)    