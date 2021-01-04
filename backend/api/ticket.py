from flask import jsonify
from flask_restx import Resource

from api import api, model
from models import db
from models.ticket import Ticket
from models.user import User
from models.category import Category
from schemas.ticket import TicketSchema


@api.route('/tickets/<int:id>')
class TicketController(Resource):
    def get(self, id):
        """ Get ticket by id """
        ticket = Ticket.query.filter_by(id == id).one()

        return jsonify(ticket)

    def delete(self, id):
        """ delete ticket by id """
        Ticket.query.filter_by(id=id).delete()
        db.session.commit()
        return None

    @api.expect(model)
    def put(self, id):
        ticket = Ticket.query.filter(Ticket.id == id).one()
        ticket = TicketSchema().load(api.payload, instance=ticket, partial=True,
                                     session=db.session)
        db.session.add(ticket)
        db.session.commit()
        return jsonify(ticket)


@api.route('/tickets/<category>')
class TicketControllerNew(Resource):
    def get(self, category):
        """ Get all tickets by category """
        category = Category.query.filter(Category.name == category).one()
        tickets = Ticket.query.filter(Ticket.category == category).all()
        return jsonify(tickets)

    @api.expect(model)
    def post(self, category):
        mock_user = User.query.first()
        category = Category.query.filter(Category.name == category).one()
        api.payload.update({'submitter': mock_user, 'category': category})
        ticket = TicketSchema().load(api.payload, session=db.session)
        category
        db.session.add(ticket)
        db.session.commit()
        return jsonify(ticket)
