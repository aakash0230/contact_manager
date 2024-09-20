from app.model import User, UserSession
from app import db
from sqlalchemy import text
from app.utlis.email_utility.send_mail import send_mail
from app.utlis.common_utils.common_utils import generate_otp
# from app.utils.clock_id_generator import ClockIDGenerator as cig
from app.utlis.common_utils.clock_id_generator import ClockIDGenerator as cig
from datetime import datetime, timedelta
import jwt, random

class AuthService:


    def generateToken(self, id):
        print(id)
        secret = "secret"
        algorithm = "HS256"
        #create session key
        session_id = self.createSession(id)
        # json.dumps(session_id, cls=UUIDEncoder)
        token = jwt.encode({'session_id': session_id, 'iat': datetime.now() - timedelta(days=1) }, secret, algorithm=algorithm)
        return token
    
    def createSession(self,id):
        cigObject = cig()
        session = cigObject.generate_id()
        print(session)
        user_session = UserSession(
            user_id=id, 
            session_key=session,
            )
        user_session.save()
        return session


    def get_otp(self, data):
        email = data.get('email')
        name = data.get('name')
        print(email)
        if email and name: 
            userDetails = db.session.query(User).filter(User.email == email).first()
            if userDetails:
                otp = generate_otp()
                userDetails.otp = otp
                User.update(userDetails)
                send_mail(userDetails.email, otp)
                return True, "OTP send to provided email_id", {}
            else:
                otp = generate_otp()
                userDetails = User(
                    email = email,
                    otp = otp,
                    name = name
                )
                userDetails.save()
                send_mail(email, otp)
                return True, "OTP send to provided email_id", {}
        else:
            return False, "Please provide email and name", {}
        
    
    def verify_otp(self, data):
        email = data.get('email')
        otp = data.get('otp')
        if email and otp:
            userDetails = db.session.query(User).filter(User.email == email).first()
            print(userDetails)
            if userDetails.otp == otp:
                userDetails = userDetails.to_dict()
                print(userDetails)
                return True, "OTP verified successfully", userDetails
            else:
                return False, "Invalid OTP", {}
        else:
            return False, "Please provide otp", {}
        
    def create_password(self, data):
        email = data.get('email')
        password = data.get('password')
        print(email, password)
        if email and password:
            userDetails = db.session.query(User).filter(User.email == email).first()
            print(userDetails)
            userDetails.password = password
            User.update(userDetails)
            print(userDetails)
            return True, "Password created successfully", {}
        else:
            return False, "Please provide Password", {}


    def login(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            userDetails = db.session.query(User).filter(User.email == email).first()
            print(userDetails)
            if userDetails and userDetails.check_password(password):
                print("cindition is true")
                token = self.generateToken(userDetails.id)
                print(token)
                if token:
                    user_session = UserSession.query.filter_by(user_id=userDetails.id).order_by(UserSession.created_on.desc()).first()
                    user_session.access_token = token
                    user_session.login_time = datetime.now()
                    user_session.save()
                    return True, "Login Successful", {"user_id" : userDetails.id, "token" : token}
                else:
                    return False, "Invalid Token", {}
            else:
                return False, "Invalid Email or Password", {}
