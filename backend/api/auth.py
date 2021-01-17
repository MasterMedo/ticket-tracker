from flask import request
from flask_restx import Resource
from flask_jwt_extended import create_access_token

from api import api, model
from models.user import User


@api.route('/auth')
class AuthController(Resource):
    @api.expect(model)
    def post(self):
        """ Login with username and password """
        data = request.get_json()
        if data is None:
            return {}, 400
        user = User.query.filter_by(username=data.get('username')).first()
        if user is None or data.get('password') != 'password':
            return {}, 401

        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}
