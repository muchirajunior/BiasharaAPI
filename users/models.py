from . import db

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    username=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(100))

    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password