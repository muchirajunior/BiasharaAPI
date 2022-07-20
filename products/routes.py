from flask import Blueprint, jsonify,request
from flask_jwt_extended import jwt_required
from schemas import *
from .services import *

products=Blueprint('products',__name__,url_prefix='/products')

@products.get('/')
@jwt_required
def getAllProducts():
    products=Product.query.all()
    products=productsSchema.dump(products)
    return jsonify(message="all products !!",data=products),200

@products.get("/<id>")
@jwt_required
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
@jwt_required
def createproduct():
    try:
        product=createNewProduct(request.json)
        db.session.add(product)
        db.session.commit()
        product=productSchema.dump(product)
        return jsonify(message="creates product successfully", data=product)

    except Exception as e:
         return jsonify(message="failed to create new product",error=str(e)),406

@products.put('/<id>')
@jwt_required()
def updateProduct(id):
    try:
        product=Product.query.filter_by(id=id).first()
        updatedProduct(request.json,product)
        db.session.commit()

        return jsonify(message="updated product successfully",data=product),200

    except Exception as e:
        return jsonify(message="failed to update product",error=str(e)),406


@products.delete('/<id>')
@jwt_required()
def deleteProduct(id):
    product:Product=Product.query.filter_by(id=id).first()
    if product==None:
        return jsonify(message="product not found"),404
    db.session.delete(product)
    db.session.commit()
    
    return jsonify(message="deleted product succesfuly"),200