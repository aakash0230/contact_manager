from app.model import PhoneSpamMapping
from app.model.base import db
from flask import g

class UserSpamService:
    def mark_as_spam(self, data):
        phone_number = data.get('phone_number')
        user_id = g.user_id
        is_spam_exists = db.session.query(PhoneSpamMapping).filter(PhoneSpamMapping.user_id == user_id, PhoneSpamMapping.phone_no == phone_number).first()
        if is_spam_exists:
            return False, "ALready marked as Spam", {}
        if user_id and phone_number:
            spam_detail = PhoneSpamMapping(
                user_id=user_id,
                phone_no = phone_number
            )

            spam_detail.save()
            return True, "Phone marked as spam", {}
        else:
            return False, "User ID or Phone Number is missing", {}
        
    def mark_as_unspam(self, data):
        phone_number = data.get('phone_number')
        user_id = g.user_id
        
        spam_detail = db.session.query(PhoneSpamMapping).filter(
            PhoneSpamMapping.user_id == user_id, 
            PhoneSpamMapping.phone_no == phone_number
        ).first()

        if spam_detail:
            # If found, delete the record marking it as unspam
            db.session.delete(spam_detail)
            db.session.commit()
            return True, "Phone unmarked as spam", {}
        else:
            # If the phone number is not marked as spam by the user
            return False, "Phone number not marked as spam", {}