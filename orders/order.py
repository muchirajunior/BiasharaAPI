from . import db

class Order(db.Model):
    __tablename__="orders"
    id=db.Column(db.Integer, primary_key=True)
    business=db.Column(db.String(200))
    product=db.Column(db.String(200))
    quantity=db.Column(db.Integer)
    client=db.Column(db.String(100))
    address=db.Column(db.String(100))
    contact=db.String(db.String(100))
    delivered=db.Column(db.Boolean,default=False)

    def __init__(self,business,product,quantity,client,address,contact):
        self.business=business
        self.product=product
        self.quantity=quantity
        self.client=client
        self.address=address
        self.contact=contact

