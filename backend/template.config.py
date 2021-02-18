import os
import datetime

SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Users\zorgo\OneDrive\1\Desktop\Nova mapa\app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", os.urandom(24))
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
