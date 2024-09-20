from flask import request, jsonify, g
from functools import wraps
import jwt
from app.model import UserSession
from app import app

app.config['SECRET_KEY'] = "secret"
app.config['JWT_ALGORITHM'] = "HS256"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Check if the 'Authorization' header is present
        if 'Authorization' in request.headers:
            bearer_token = request.headers['Authorization']
            if bearer_token.startswith('Bearer '):
                token = bearer_token.split(" ")[1]

        if not token:
            return jsonify({'status':200, 'message': 'Token is missing!'}), 200

        try:
            # Decode the token
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[app.config['JWT_ALGORITHM']])
            # Attach user information to the request context (g)
            # g.user_id = payload['user_id']
            g.user_id = None
            session_key = payload['session_id']
            user_session = UserSession.query.filter_by(session_key=session_key).order_by(UserSession.created_on.desc()).first()
            if not user_session or user_session.access_token != token or user_session.is_logged_out == 1:
                raise jwt.InvalidTokenError
            else:
                g.user_id = user_session.user_id
                g.user_session_id = user_session.id
            
            
        except jwt.ExpiredSignatureError:
            return jsonify({'status': 200,'message': 'Token has expired!'}), 200
        except jwt.InvalidTokenError:
            return jsonify({'status': 200,'message': 'Invalid token!'}), 200

        return f(*args, **kwargs)

    return decorated
