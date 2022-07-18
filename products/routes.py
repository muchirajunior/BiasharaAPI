from flask import Blueprint, jsonify
from .product import *

products=Blueprint('products',__name__,url_prefix='/products')

@products.get('/')
def getAllProducts():
    return jsonify(message="all products !!")