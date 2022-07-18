from sqlalchemy import JSON
from . import db

class Business(db.Model):
    __tablename__="businesses"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    username=db.Column(db.String(50),unique=True,nullable=False)
    location=db.Column(db.String(50))
    cartegory=db.Column(db.String(100))
    phone=db.Column(db.String(20),unique=True)
    password=db.Column(db.String(100))
    photo=db.Column(db.String)
    site=db.Column(db.String(300))
    subscription=db.Column(db.Float(10),default=100)
    productCartegories=db.Column(JSON)

    def __init__(self,name,username,location,cartegory,phone,password,photo,site):
        self.name=name
        self.username=username
        self.location=location
        self.cartegory=cartegory
        self.phone=phone
        self.password=password
        self.photo=photo
        self.site=site