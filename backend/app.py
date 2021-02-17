import os
from datetime import datetime, timedelta

from flask import Flask
from flask.json import JSONEncoder

from flask_marshmallow import Marshmallow
from flask_cors import CORS

from models import db
from api import api_bp, jwt
from api.accounttype import *  # noqa
from api.auth import *  # noqa
from api.category import *  # noqa
from api.comment import *  # noqa
from api.label import *  # noqa
from api.ticket import *  # noqa
from api.user import *  # noqa


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == timedelta:
            return str(o)
        elif type(o) == datetime:
            return o.isoformat()
        else:
            return super().default(o)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\zorgo\OneDrive\1\Desktop\Nova mapa\app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", os.urandom(24))
app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", os.urandom(24))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)
app.json_encoder = CustomJSONEncoder
db.app = app
db.init_app(app)
ma = Marshmallow(app)
CORS(app)
app.register_blueprint(api_bp)
jwt.init_app(app)

if __name__ == '__main__':
    app.run(host='192.168.0.155', port=5000, debug=True)
