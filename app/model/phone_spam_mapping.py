from app.model.base import BaseModel, db

class PhoneSpamMapping(BaseModel):
    __tablename__ = "phone_spam_mapping"
    user_id = db.Column(db.Integer, nullable = True)
    phone_no = db.Column(db.String(50), nullable = True)