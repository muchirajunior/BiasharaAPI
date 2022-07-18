from flask import Blueprint, jsonify
from .order import *
orders=Blueprint('orders',__name__,'/orders')

@orders.get('/')
def getAllOrders():

    return jsonify(message="all orders !!")