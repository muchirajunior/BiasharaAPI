from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required

from schemas import *
from .services import *

business=Blueprint('business',__name__,url_prefix='/business')

@business.get('/')
def getAllBusiness():
    businesses=Business.query.all()
    businesses=businessesSchema(businesses)
    return jsonify(message='all business in the records',data=businesses)

@business.get('/<username>')
def getBusinessByUsername(username:str):
    
    return jsonify(message=f"business with username {username}")

@business.post('/')
def createBusiness():
    try:
        business:Business=createNewBusiness(request.json)
        db.session.add(business)
        db.session.commit()
        return jsonify(message="business created successfuly", data=business),201
    except:
        jsonify(message="failed to create business"),406