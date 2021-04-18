from sqlalchemy.orm import sessionmaker
from db import Product , engine
Session =  sessionmaker(bind=engine)
session = Session()
p = Product(code = 'IPX',name = 'IPhoneX',price = '15000000')
session.add(p)
session.commit()

p = session.query(Product).filter(Product.code == 'IPX').first()
print(p.name)
