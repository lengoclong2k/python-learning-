# from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import create_engine
from urllib.parse import quote
Base = declarative_base()
# password = quote('abc@123')
engine = create_engine('sqlite:///:memory:',echo = True)

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key = True)
    code = Column(String(20))
    name = Column(String(100))
    price = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind= engine)

session = Session()
p = Product()
p.id = 0
p.code = 'IPX'
p.name = 'IPhoneX'
p.price = 15000000
session.add(p)
session.commit()
p = session.query(Product).all()
for p in Product:
    print(f'Dien thoai {p.name} co ma code {p.code} co gia la {p.price} co id {p.id}')

session.close()