from flask import Blueprint, jsonify,request
from schemas import *
from .services import *

products=Blueprint('products',__name__,url_prefix='/products')

@products.get('/')
def getAllProducts():
    products=Product.query.all()
    products=productsSchema.dump(products)
    return jsonify(message="all products !!",data=products),200

@products.get("/<id>")
def getProductById(id:int):
    try:
        product=Product.query.filter_by(id=id).first()
        if product==None:
            return jsonify(message="no such product in the records"),404
        product=productSchema.dump(product)
        print(product)
        return jsonify(product),200
    except Exception as e:
        return jsonify(message="failed to get product",error=str(e)),406

@products.post("/")
def createproduct():
    try:
        product=createNewProduct(request.json)
        db.session.add(product)
        db.session.commit()
        product=productSchema.dump(product)
        return jsonify(message="creates product successfully", data=product)

    except Exception as e:
         return jsonify(message="failed to create new product",error=str(e)),406