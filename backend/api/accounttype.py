from flask import jsonify
from flask_restx import Resource

from api import api, model
from models import db
from models.accounttype import Accounttype
from schemas.accounttype import AccounttypeSchema


@api.route('/accounttypes/<accounttype>')
class AccounttypeController(Resource):
    def get(self, accounttype):
        """ Get account type by account type name """
        accounttype = Accounttype.query\
                                 .filter(Accounttype.name == accounttype).one()
        return jsonify(accounttype)

    @api.expect(model)
    def put(self, accounttype):
        """ Edit account type by account type name """
        accounttype = Accounttype.query\
                                 .filter(Accounttype.name == accounttype).one()
        accounttype = AccounttypeSchema().load(api.payload, partial=True,
                                               session=db.session,
                                               instance=accounttype)
        db.session.add(accounttype)
        db.session.commit()
        return jsonify(accounttype)

    def delete(self, accounttype):
        """ Delete account type by account type name """
        accounttype = Accounttype.query\
                                 .filter(Accounttype.name == accounttype).one()
        db.session.delete(accounttype)
        db.session.commit()
        return jsonify(accounttype)


@api.route('/accounttypes/')
class AccounttypeControllerNew(Resource):
    @api.expect(model)
    def post(self):
        accounttype = AccounttypeSchema().load(api.payload, session=db.session)
        db.session.add(accounttype)
        db.session.commit()
        return jsonify(accounttype)
