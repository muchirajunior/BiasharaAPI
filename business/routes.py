from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required

from schemas import *
from .services import *

business=Blueprint('business',__name__,url_prefix='/business')

@business.get('/')
def getAllBusiness():
    try:
        businesses=Business.query.all()
        businesses=businessesSchema.dump(businesses)
        return jsonify(message='all business in the records',data=businesses)
    except Exception as e:
        return jsonify(maessage="failed to get all business data",error=str(e)),406

@business.get('/<username>')
def getBusinessByUsername(username:str):
    business=Business.query.filter_by(username=username).first()
    business=businessSchema.dump(business)
    business:dict=business.pop("orders")
    return jsonify(business)

@business.post('/')
def createBusiness():
    try:
        print(request.json)
        business:Business=createNewBusiness(request.json)
        db.session.add(business)
        db.session.commit()
        return jsonify(message="business created successfuly", data=business),201
    except Exception as e:
        return jsonify(message="failed to create business", error=str(e)),406