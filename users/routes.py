from flask import Blueprint, jsonify
from .models import *
users=Blueprint('users',__name__,url_prefix='/users')

@users.get('/')
def getAllUsers():

    return jsonify(message="all users !!!!!")