from flask import jsonify
from flask_restx import Resource

from api import api, model
from models import db
from models.user import User
from models.accounttype import Accounttype
from schemas.user import UserSchema


@api.route('/users/<username>')
class UserController(Resource):
    def get(self, username):
        """ Get user by username """
        user = User.query.filter(User.username == username).one()
        return jsonify(user)

    def delete(self, username):
        """ Delete user by username """
        user = User.query.filter(User.username == username).one()
        db.session.delete(user)
        db.session.commit()
        return jsonify(user)

    @api.expect(model)
    def put(self, username):
        """ Edit user by username """
        user = User.query.filter(User.username == username).one()
        user = UserSchema().load(api.payload,
                                 instance=user,
                                 partial=True,
                                 session=db.session)
        db.session.add(user)
        db.session.commit()
        return jsonify(user)


@api.route('/register/<accounttype>')
class UserControllerNew(Resource):
    @api.expect(model)
    def post(self, accounttype):
        """ Create <accounttype> user """
        accounttype = Accounttype.query\
                                 .filter(Accounttype.name == accounttype).one()
        api.payload['accounttype'] = accounttype
        user = UserSchema().load(api.payload, session=db.session)
        db.session.add(user)
        db.session.commit()
        return jsonify(user)
