from flask import jsonify, request
from app.services.user_phone_services import  UserPhoneService
userPhoneService = UserPhoneService()

class UserPhoneController:
    def add_phone_number(self):
        try:
            data = request.get_json()
            print(data)
            status, message, result = userPhoneService.add_phone_number(data)
            return jsonify({"status" : status, "message" : message, "data" : result})
        except Exception as e:
            return jsonify({"status" : False, "message" : str(e), "data" : {}})
        
    def get_phone_number(self):
        try:
            status, message, result = userPhoneService.get_phone_number()
            return jsonify({"status" : status, "message" : message, "data" : result})
        except Exception as e:
            return jsonify({"status" : False, "message" : str(e), "data" : {}})

