from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import create_engine
from urllib.parse import quote
db_host = 'localhost'
db_user = 'admin'
db_pass = quote('abc@123')  #abc%40123 encode
db_name = 'longpython'
conn_url = f'mysql://{db_user}:{db_pass}@{db_host}/{db_name}?charset=utf8'
print(conn_url)
Base = declarative_base()
engine = create_engine(conn_url)
Session = sessionmaker(bind= engine)
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer,primary_key = True)
    name = Column(String(100))
    alias = Column(String(100))
class Book(Base):
    __tablename__ = 'book'
    id  = Column(Integer,primary_key = True)
    code = Column(String(100))
    name = Column(String(100))
    qty = Column(Integer)
    author_id = Column(Integer,ForeignKey('author.id'))


if __name__== '__main__':
    session = Session()
    Base.metadata.create_all(engine)