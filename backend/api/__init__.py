from collections import defaultdict

from flask import Blueprint
from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError

api_bp = Blueprint("api", __name__)
api = Api(api_bp, version='0.1', title='Tickets Api',
          description='Api for the Tickets app.')

model = api.model('', defaultdict())


@api.errorhandler(NoResultFound)
def handle_no_result_error(error):
    '''Return a custom not found error message and 404 status code'''
    return {'message': str(error)}, 404


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    '''Return a custom not found error message and 404 status code'''
    return {'message': str(error)}, 404
