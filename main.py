from datetime import timedelta
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']="Hbfj@hy**^HGEERI56B3aa;7y(gertY64H55!"
app.config["JWT_SECRET_KEY"] = "FJVDJH93623FDNJHGS537KDGN6@#$%JJ"
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(hours=10)

db=SQLAlchemy(app)
ma=Marshmallow(app)
bycrypt=Bcrypt(app)
jwt= JWTManager(app)