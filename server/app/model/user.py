from app.model.base import BaseModel, db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(BaseModel):
    __tablename__ = "user"
    status = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    phone_no = db.Column(db.String(50), nullable=True)
    _password = db.Column(db.String(200), nullable=True)
    otp = db.Column(db.String(50), nullable=True)
    

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        if plaintext_password:
            self._password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')
        else:
            self._password = None

    def check_password(self, plaintext_password):
        return bcrypt.check_password_hash(self._password, plaintext_password)