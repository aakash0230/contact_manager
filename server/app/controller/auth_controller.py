from app.services.auth_service import AuthService
from flask import request, jsonify


authService = AuthService()

class AuthController:
    def get_otp(self):
        try:
            data = request.get_json()
            status, message, result = authService.get_otp(data)
            return jsonify({"status" : status, "message" : message, "data" : result})
        except Exception as e:
            return jsonify({"status" : False, "message" : str(e), "data" : result})
        

    def verify_otp(self):
        try:
            data = request.get_json()
            status, message, result = authService.verify_otp(data)
            return jsonify({"status" : status, "message" : message, "data" : result})
        except Exception as e:
            return jsonify({"status" : False, "message" : str(e), "data" : {}})
        
    def create_password(self):
        try:
            data = request.get_json()
            status, message, result = authService.create_password(data)
            return jsonify({"status" : status, "message" : message, "data" : result})
        except Exception as e:
            return jsonify({"status" : False, "message" : str(e), "data" : {}})
        
    def login(self):
        try:
            data = request.get_json()
            status, message, result = authService.login(data)
            return jsonify({"status" : status, "message" : message, "data" : result})
        except Exception as e:
            return jsonify({"status" : False, "message" : str(e), "data" : {}})
            
