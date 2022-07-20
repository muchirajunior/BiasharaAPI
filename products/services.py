import json

from .models import db,Product

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

def updatedProduct(data:json,product:Product):
    product.name=data['name'],
    product.price=data['price'],
    product.description=data['description'],
    product.photo=data['photo'],
    product.type=data['type'],
    product.photo_2=data['photo_2']
    product.quantity=data['quantity']
    product.photo_3=data['photo_3']

