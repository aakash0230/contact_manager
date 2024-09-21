from app.model.base import BaseModel, db


class UserSession(BaseModel):
    __tablename__= "user_session"
    status = db.Column(db.String(50), nullable=True)
    session_key = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    is_logged_out = db.Column(db.Boolean, nullable=False, default = False)
    logout_time = db.Column(db.DateTime, nullable=True)
    login_time = db.Column(db.DateTime, nullable=True)
    access_token = db.Column(db.String(4000), nullable=True)
