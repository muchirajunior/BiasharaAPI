from flask import Blueprint,jsonify
from flask_jwt_extended import jwt_required
from .business import *

business=Blueprint('business',__name__,url_prefix='/business')

@business.get('/')
def getAllBusiness():

    return jsonify(message='all business in the records')

@business.get('/<username>')
@jwt_required()
def getBusinessByUsername(username:str):
    
    return jsonify(message=f"business with username {username}")