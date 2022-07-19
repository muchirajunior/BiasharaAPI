from flask import Blueprint, jsonify,request

from orders.services import createNewOrder
from .models import *
from  schemas import *
orders=Blueprint('orders',__name__,url_prefix='/orders')

@orders.get('/')
def getAllOrders():
    try:
        orders=Order.query.all()
        orders=ordersSchema.dump(orders)

        return jsonify(message="all orders !!",data=orders)
    except Exception as e:
        return jsonify(message="error fetching data", error=str(e))

@orders.get('/<id>')
def getOrderById(id):
    try:
        order=Order.query.filter_by(id=id).first()
        if order==None:
            return jsonify(message="no such order in our record"),404
        order=orderSchema.dump(order)
        print(order)

        return jsonify(order)
    except Exception as e:
        return jsonify(message="error fetching data", error=str(e))

@orders.post('/')
def createOrder():
    try:
        order=createNewOrder(request.json)
        db.session.add(order)
        db.session.commit()
        order=orderSchema.dump(order)

        return jsonify(message="order created successfuly",data=order),201
    except Exception as e:
        return jsonify(message="failed to create new order",error=str(e)),406