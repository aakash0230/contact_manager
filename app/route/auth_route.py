from flask import Blueprint, jsonify
from app.controller.auth_controller import AuthController

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

