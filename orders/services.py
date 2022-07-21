import json

import requests
from .models import db,Order
from . import Business

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

def sendMessage(order:Order):
    try:
        business:Business=Business.query.filter_by(id=order.businessid).first()
        products=""
        for item in order.products['products']:
            products+=item+", "

        message=f"Hello {business.name} a new order by {order.client} with {products} from {order.address} total price ksh {order.total_price}. Thank You. "
        url="https://my.jisort.com/messenger/send_message/?"
        url+=f"username=muchirajunior&password=junior@12&recipients={business.phone}=&message={message}"
        requests.get(url)
    except:
        pass