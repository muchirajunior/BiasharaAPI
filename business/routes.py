from random import randint
from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required
from orders.models import Order
from products.models import Product

from schemas import *
from .services import *

business=Blueprint('business',__name__,url_prefix='/business')

@business.get('/')
@jwt_required()
def getAllBusiness():
    try:
        businesses=Business.query.all()
        businesses=businessesSchema.dump(businesses)
        return jsonify(message='all business in the records',data=businesses),200
    except Exception as e:
        return jsonify(maessage="failed to get all business data",error=str(e)),406

@business.get('/<username>')
def getBusinessByUsername(username:str):
    business=Business.query.filter_by(username=username).first()
    if business == None:
        return jsonify(message="no such business in the records"),404
    business=publicBusinessSchema.dump(business)
    return jsonify(business),200

@business.post('/')
def createBusiness():
    try:
        business:Business=createNewBusiness(request.json)
        db.session.add(business)
        db.session.commit()
        business=businessSchema.dump(business)
        return jsonify(message="business created successfuly", data=business),201
    except Exception as e:
        return jsonify(message="failed to create business", error=str(e.args)),406

@business.post("/signup")
def signUp():
    try:
        username=request.json['username']
        password=request.json['password']
        business=Business.query.filter_by(username=username).first()
        if business == None:
            return jsonify(message="no such business in the record!"),404
        if checkPassword(password,business.password):
            jwt_token=generateJwt(business)
            business=businessSchema.dump(business)
            return jsonify(message="login user successful",data=business,token=jwt_token),200
        else:
            return jsonify(message="wrong password"),406
    except Exception as e:
        return jsonify(message="failed to signup", error=str(e)),406

@business.post("/cartegories")
@jwt_required()
def addProductCartegory():
    try:
        business_id=request.json['business_id']
        cartegory=request.json['cartegory']
        business:Business=Business.query.filter_by(id=business_id).first()
        if business.products_cartegories == None:
            business.products_cartegories={"cartegories":[cartegory]}
        else:
            cartegories:list=business.products_cartegories['cartegories']
            business.products_cartegories=None
            db.session.commit()
            cartegories.append(cartegory)
            business.products_cartegories={"cartegories":cartegories}
            
        db.session.commit()
        return jsonify(message="added cartegory sucessfuly", cartegories=business.products_cartegories),200
    except Exception as e:
        return jsonify(message="failed to add cartegory",error=str(e)),406

@business.delete("/cartegories")
@jwt_required()
def deleteProductCartegory():
    try:
        business_id=request.json['business_id']
        cartegory=request.json['cartegory']
        business:Business=Business.query.filter_by(id=business_id).first()
        cartegories:list=business.products_cartegories['cartegories']
        business.products_cartegories=None
        db.session.commit()
        cartegories.remove(cartegory)
        business.products_cartegories={"cartegories":cartegories}
            
        db.session.commit()
        return jsonify(message="deleted cartegory sucessfuly", cartegories=business.products_cartegories),200
    except Exception as e:
        return jsonify(message="failed to delete cartegory",error=str(e)),406

@business.put('/<id>')
@jwt_required()
def updateBusiness(id):
    try:
        business:Business=Business.query.filter_by(id=id).first()
        business.name=request.json['name']
        business.address=request.json['address']
        business.phone=request.json['phone']
        business.website=request.json['website']
        business.photo=request.json['photo']
        business.pdf_menu=request.json['pdf_menu']
        db.session.commit()

        return jsonify(message="updated business profile successfuly",data=business),200
    except Exception as e:
        return jsonify(message="failed to update",error=str(e.args)),406

@business.get('/password/<username>')
def forgotPassword(username):
    try:
        business=Business.query.filter((Business.username==username) | (Business.phone==str(username))).first()
        if business== None:
            return jsonify("business not found"),404
        pin=Pin.query.filter_by(contact=business.phone).first()
        if pin !=None:
            db.session.delete(pin)
            db.session.commit()
        randomPin=randint(100000,999999)
        db.session.add(Pin(business.phone,randomPin))
        db.session.commit()
        sendMessage(business.phone,randomPin)
        return jsonify(message="request sent"),200
    except Exception as e:
        return jsonify(message="request",error=str(e.args)),406

@business.patch("/password")
def changePassword():
    try:
        userPin=request.json['pin']
        password=request.json['password']
        pin:Pin=Pin.query.filter_by(pin=userPin).first()
        if pin==None:
            return jsonify(message="invalid pin"),406
        business:Business=Business.query.filter_by(phone=pin.contact).first()
        business.password=createhashPassword(password)
        db.session.delete(pin)
        db.session.commit()

        return jsonify(message="password changed successfully"),200
    except Exception as e:
        return jsonify(message="failed to update",error=str(e.args)),406

@business.delete('/<id>')
@jwt_required()
def deleteBusiness(id):
    try:
        business=Business.query.filter_by(id=id).first()
        products=Product.query.filter_by(businessid=id).all()
        orders=Order.query.filter_by(businessid=id).all()
        db.session.delete(business)
        for product in products:
            db.session.delete(product)
        for order in orders:
            db.session.delete(order)
        db.session.commit()


        return jsonify(message="deleted business successfly"),200
    except Exception as e:
        return jsonify(message="failed to delete business",error=str(e.args)),406