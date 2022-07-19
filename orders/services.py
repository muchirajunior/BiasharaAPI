import json
from .order import db,Order

def createNewOrder(data:json):
    order:Order=Order(
        products=data['products'],
        total_price=data["total_price"],
        client=data['client'],
        address=data['address'],
        contact=data['contact'],
        businessid=data['businessid']
    )

    return order
