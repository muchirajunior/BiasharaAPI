from datetime import datetime
from sqlalchemy import JSON
from . import db

class Order(db.Model):
    __tablename__="orders"
    id=db.Column(db.Integer, primary_key=True)
    products=db.Column(JSON)
    total_price=db.Column(db.Float)
    client=db.Column(db.String(100))
    address=db.Column(db.String(100))
    contact=db.String(db.String(100))
    complete=db.Column(db.Boolean,default=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    businessid=db.Column(db.Integer,db.ForeignKey('business.id'),nullable=False)

    def __init__(self,product,total_price,client,address,contact,businessid):
        self.businessid=businessid
        self.product=product
        self.total_price=total_price
        self.client=client
        self.address=address
        self.contact=contact

