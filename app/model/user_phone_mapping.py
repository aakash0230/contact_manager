from app.model.base import BaseModel, db

class UserPhoneMapping(BaseModel):
    __tablename__ = "user_phone_mapping"
    user_id = db.Column(db.Integer, nullable=True)
    phone_no = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(50), nullable=True)