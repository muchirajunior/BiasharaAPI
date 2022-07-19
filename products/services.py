import json
from .product import db,Product

def createNewProduct(data:json):
    product:Product=Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        photo=data['photo'],
        type=data['type'],
        businessid=data['businessid']
    )

    return product
