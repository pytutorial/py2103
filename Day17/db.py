from sqlalchemy import Column, Integer, String,\
         DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote
Base = declarative_base()

db_host = '34.122.175.106'       #/phpmyadmin
db_user = 'test'                 # localhost (admin)
db_pass = quote('abc@123')       # abc%40123
db_name = 'py2103'  # tao rieng
conn_url= f'mysql://{db_user}:{db_pass}@{db_host}/{db_name}' \
            + '?charset=utf8'

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    alias = Column(String(100))
    def __repr__(self): 
        return self.name

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    code = Column(String(30))
    name = Column(String(200))
    qty = Column(Integer)
    author_id = Column(Integer, ForeignKey('author.id'))

engine = create_engine(conn_url)
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    #session = Session()
    Base.metadata.create_all(engine)