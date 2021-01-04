from datetime import datetime, timedelta

from flask import Flask
from flask.json import JSONEncoder

from flask_marshmallow import Marshmallow
from flask_cors import CORS

from models import db
from api import api_bp
from api.accounttype import *
from api.user import *
from api.ticket import *
from api.category import *
from api.comment import *
from api.label import *


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == timedelta:
            return str(o)
        elif type(o) == datetime:
            return o.isoformat()
        else:
            return super().default(o)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test13.db'
app.json_encoder = CustomJSONEncoder
db.app = app
db.init_app(app)
ma = Marshmallow(app)
CORS(app)
app.register_blueprint(api_bp)


if __name__ == '__main__':
    app.run(debug=True)
