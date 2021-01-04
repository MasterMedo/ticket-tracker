from flask import jsonify
from flask_restx import Resource

from api import api, model
from models import db
from models.label import Label
from schemas.label import LabelSchema


@api.route('/labels/<int:id>')
class LabelController(Resource):
    def get(self, id):
        """ Get label by id """
        label = Label.query.filter(Label.id == id).one()
        return jsonify(label)

    def delete(self, id):
        """ Delete label by id """
        label = Label.query.filter(Label.id == id).one()
        db.session.delete(label)
        db.session.commit()
        return jsonify(label)

    @api.expect(model)
    def put(self, id):
        """ Edit label by id """
        label = Label.query.filter(Label.id == id).one()
        label = LabelSchema().load(api.payload, instance=label, partial=True,
                                   session=db.session)
        db.session.add(label)
        db.session.commit()
        return jsonify(label)


@api.route('/labels/')
class LabelControllerNew(Resource):
    @api.expect(model)
    def post(self):
        label = LabelSchema().load(api.payload, session=db.session)
        db.session.add(label)
        db.session.commit()
        return jsonify(label)
