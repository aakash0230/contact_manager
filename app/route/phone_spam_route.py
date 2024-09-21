from flask import Blueprint, jsonify, g
from app.controller.phone_spam_controller import PhoneSpamController
from app.middleware.auth_middleware import token_required

phoneSpamController = PhoneSpamController()

phone_spam_bp = Blueprint('phone_spam', __name__)

@phone_spam_bp.route('/phoneSpam/markSpam', methods=['POST'])
@token_required
def mark_as_spam():
    return phoneSpamController.mark_as_spam()

@phone_spam_bp.route('/phoneSpam/markUnSpam', methods=['POST'])
@token_required
def mark_as_unspam():
    return phoneSpamController.mark_as_unspam()