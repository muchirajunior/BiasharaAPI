from . import db

class Product(db.Model):
    __tablename__='products'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    price=db.Column(db.Float,nullable=False)
    description=db.Column(db.String)
    photo=db.Column(db.String,nullable=False)
    businessid=db.Column(db.Integer,nullable=False)
    businessname=db.Column(db.String(200))

    def __init__(self,name,price,description,photo,businessid,businessname):
        self.name=name
        self.price=price
        self.description=description
        self.photo=photo
        self.businessid=businessid
        self.businessname=businessname