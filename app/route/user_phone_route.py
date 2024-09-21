from flask import Blueprint, jsonify, g
from app.controller.user_phone_controller import UserPhoneController
from app.middleware.auth_middleware import token_required

userPhoneController = UserPhoneController()

user_phone_bp = Blueprint('user_phone', __name__)

@user_phone_bp.route('/userPhone/addNumber', methods=['POST'])
@token_required
def add_phone_number():
    return userPhoneController.add_phone_number()

@user_phone_bp.route('/userPhone/getNumber', methods=['POST'])
@token_required
def get_phone_number():
    return userPhoneController.get_phone_number()