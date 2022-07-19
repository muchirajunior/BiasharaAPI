from datetime import datetime
from sqlalchemy import JSON
from . import db

class Business(db.Model):
    __tablename__="businesses"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    username=db.Column(db.String(50),unique=True,nullable=False)
    address=db.Column(db.String(200))
    cartegory=db.Column(db.String(100))
    phone=db.Column(db.String(20),unique=True)
    password=db.Column(db.String(100))
    photo=db.Column(db.String(200))
    pdf_menu=db.Column(db.String(200))
    website=db.Column(db.String(300))
    subscription=db.Column(db.Float,default=100)
    active=db.Column(db.Boolean,default=True)
    products_cartegories=db.Column(JSON)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    products=db.relationship("Product",backref='businesses',lazy=True)
    orders=db.relationship("Order",backref='businesses',lazy=True)

    def __init__(self,name,username,address,cartegory,phone,password,photo,website):
        self.name=name
        self.username=username
        self.address=address
        self.cartegory=cartegory
        self.phone=phone
        self.password=password
        self.photo=photo
        self.website=website

class Pin(db.Model):
    __tablename__="pins"
    id=db.Column(db.Integer, primary_key=True)
    contact=db.Column(db.String(20),nullable=False)
    pin=db.Column(db.Integer)

    def __init__(self,contact,pin):
        self.contact=contact
        self.pin=pin