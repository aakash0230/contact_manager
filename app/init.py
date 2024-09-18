from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

CORS(app)
bcrypt = Bcrypt(app)


app.config["env"] = os.getenv('ENV')
# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('RDS_HOST')}/{os.getenv('DB_NAME')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db, directory="db/migrations")

from app.model import *

from app.route import __all__ as all_blue_print
from app.route import *
for route_bp in all_blue_print:
    app.register_blueprint(globals()[route_bp])

from app.middleware.route_middleware import check_route_exists

app.before_request(check_route_exists(app))

# Register error handlers
from app.error_handlers import handle_bad_request, handle_not_found, handle_internal_server_error
app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, handle_not_found)
app.register_error_handler(500, handle_internal_server_error)
@app.errorhandler(Exception)
def handle_generic_error(e):
    return handle_internal_server_error(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))