from . import db

class Product(db.Model):
    __tablename__='products'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    price=db.Column(db.Float,nullable=False)
    description=db.Column(db.String)
    type=db.Column(db.String(10),nullable=False)
    photo=db.Column(db.String,nullable=False)
    quantity=db.Column(db.String(20))
    photo_2=db.Column(db.String)
    photo_3=db.Column(db.String)
    businessid=db.Column(db.Integer,db.ForeignKey('business.id'),nullable=False)
    

    def __init__(self,name,price,description,photo,type,businessid):
        self.name=name
        self.price=price
        self.description=description
        self.photo=photo
        self.type=type
        self.businessid=businessid