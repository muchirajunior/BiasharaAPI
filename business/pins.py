from . import db

class Pin(db.Model):
    __tablename__="pins"
    id=db.Column(db.Integer, primary_key=True)
    contact=db.Column(db.String(20),nullable=False)
    pin=db.Column(db.Integer)

    def __init__(self,contact,pin):
        self.contact=contact
        self.pin=pin
