import json
from .business import Business,db
from . import bycrypt

def createhashPassword(password:str):
    password= bycrypt.generate_password_hash(password,10).decode(encoding='utf-8')

    return password

def checkPassword(enteredPassword, storedPassword):
    return bycrypt.check_password_hash(str.encode(storedPassword),enteredPassword)

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