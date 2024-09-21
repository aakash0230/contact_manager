from flask import jsonify, request
from app.services.user_spam_services import UserSpamService
from app.middleware.auth_middleware import token_required

userSpamService = UserSpamService()

class PhoneSpamController:
    def mark_as_spam(self):
        try:
            data = request.get_json()
            status, message, result = userSpamService.mark_as_spam(data)
            return jsonify({"status" : status, "message" : message, "data" : result})
        except Exception as e:
            return jsonify({"status" : False, "message" : str(e), "data" : {}})
        
    def mark_as_unspam(self):
        try:
            data = request.get_json()
            status, message, result = userSpamService.mark_as_unspam(data)
            return jsonify({"status" : status, "message" : message, "data" : result})
        except Exception as e:
            return jsonify({"status" : False, "message" : str(e), "data" : {}})
