import json
from flask_jwt_extended import create_access_token
from .business import Business,db
from . import bycrypt

def createhashPassword(password:str):
    password= bycrypt.generate_password_hash(password,10).decode(encoding='utf-8')

    return password

def checkPassword(enteredPassword, storedPassword):
    print(type(storedPassword))
    return bycrypt.check_password_hash(storedPassword.encode("utf-8"),enteredPassword)

def createNewBusiness(data:json):
    business=Business(
        name=data['name'],
        username=data['username'],
        address=data['address'],
        cartegory=data['cartegory'],
        phone=data['phone'],
        password=createhashPassword(data['password']),
        photo=data['photo'],
        website=data['website']
    )

    return business

def generateJwt(business:Business):
    user={
        "username":business.username,
        "name":business.name,
        "website":business.website,
        "address":business.address,
        "cartegory":business.cartegory
    }

    token =create_access_token(identity=user)

    return token