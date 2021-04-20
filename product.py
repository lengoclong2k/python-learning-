from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

from sqlalchemy import create_engine
from urllib.parse import quote
db_host = 'localhost'
db_user = 'admin'
db_pass = quote('abc@123')  #abc%40123 encode
db_name = 'product_test'
conn_url = f'mysql://{db_user}:{db_pass}@{db_host}/{db_name}?charset=utf8'
print(conn_url)
Base = declarative_base()
engine = create_engine(conn_url)
Session = sessionmaker(bind= engine)
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer,primary_key=True)
    code = Column(String(100),unique= True)
    name = Column(String(100))
    price = Column(Integer)
class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    phone  = Column(Integer)
    add = Column(String(100))
class Order(Base):
    __tablename__ = 'pos_order'
    id = Column(Integer,primary_key=True)
    customer_id  = Column(Integer,ForeignKey('customer.id'))
    customer = relationship('Customer')
    date = Column(DateTime)
class OrderItem(Base):
    __tablename__ = 'pos_order_item'
    id = Column(Integer,primary_key = True)
    order_id = Column(Integer,ForeignKey('pos_order.id'))
    order = relationship('Order')
    product_id = Column(Integer,ForeignKey('product.id'))
    product = relationship('Prodcut')
    qty = Column(Integer)
    price_unit = Column(Integer)

def getProductByCode(session,code) -> Product:
    return  session.query(Product)\
            .filter(Product.code== code)\
            .first()
def getCustomerByPhone(session,phone) -> Customer:
    return session.query(Customer)\
            .filter(Customer.phone == phone)\
            .first()
# def saveCustomer(session,phone) -> Customer:
#     pass
def saveOrder(session,customer_phone):
    order = Order()
    order.date = datetime.now()
    order.customer =getCustomerByPhone(customer_phone) 
    session.add(order)
    session.commit()

def saveItem(session,order_id,product_code,qty):
    item = OrderItem()
    item.date = datetime.now()
    item.order = a


if __name__ == '__main__':
    Base.metadata.create_all(engine)