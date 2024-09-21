from flask import Blueprint, jsonify, g
from app.controller.auth_controller import AuthController
from app.middleware.auth_middleware import token_required

authController = AuthController()

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/getOtp', methods=['POST'])
def login():
    return authController.get_otp()

@auth_bp.route('/auth/verifyOtp',methods=['POST'])
def verify_otp():
    return authController.verify_otp()

@auth_bp.route('/auth/createPassword', methods=['POST'])
def create_password():
    return authController.create_password()

@auth_bp.route('/auth/login', methods=['POST'])
def loign():
    return authController.login()

@auth_bp.route('/auth/protected', methods=['POST'])
@token_required
def protected():
    print(g.user_id)
    return jsonify({'message': 'This is a protected route'}), 200

