import json
from .business import Business,db
from . import bycrypt

def createhashPassword(password:str):
    password= bycrypt.generate_password_hash(password,10)

    return password


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