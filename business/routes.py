from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required

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
    business=businessSchema.dump(business)
    business:dict=business.pop("orders")
    return jsonify(business),200

@business.post('/')
def createBusiness():
    try:
        business:Business=createNewBusiness(request.json)
        db.session.add(business)
        db.session.commit()
        return jsonify(message="business created successfuly", data=business),201
    except Exception as e:
        return jsonify(message="failed to create business", error=str(e)),406

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
        return jsonify(message="added cartegory sucessfuly", cartegories=business.products_cartegories)
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
        return jsonify(message="deleted cartegory sucessfuly", cartegories=business.products_cartegories)
    except Exception as e:
        return jsonify(message="failed to delete cartegory",error=str(e)),406



