from flask import jsonify, request
from flask_restx import Resource
from sqlalchemy import and_

from api import api, model
from models import db
from models.ticket import Ticket
from models.user import User
from models.category import Category
from models.label import Label
from schemas.ticket import TicketSchema


@api.route('/tickets/<int:id>')
class TicketController(Resource):
    def get(self, id):
        """ Get ticket by id """
        ticket = Ticket.query.filter_by(id=id).one()

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


@api.route('/tickets/')
class TicketControllerN(Resource):
    @api.doc(params={
        'category': {'in': 'query', 'description': 'ticket category (e.g. questions)'},
        'label': {'in': 'query', 'description': 'one of the labels a ticket must contain (e.g. enhancement)'},
        'submitter': {'in': 'query', 'description': 'submitter username (e.g. mastermedo)'},
        'answered': {'in': 'query', 'description': 'true or false (e.g. true)'},
        # 'project': {'in': 'query', 'description': 'project name (e.g. typetest)'},
        # 'sort': {'in': 'query', 'description': 'parameters to sort by (e.g. submitter+asc,category+desc)', 'default': 'updated+asc'},
        # 'count': {'in': 'query', 'description': 'number of records (e.g. 10)'},
    })
    def get(self):
        """ Get all tickets, filter by query """
        filters = []
        if 'category' in request.args:
            category_id = Category.query\
                .filter(Category.name == request.args['category']).one().id
            filters.append(Ticket.category_id == category_id)
        if 'submitter' in request.args:
            submitter_id = User.query\
                .filter(User.username == request.args['submitter']).one().id
            filters.append(Ticket.submitter_id == submitter_id)
        if 'answered' in request.args:
            answered = request.args['answered'] == 'true'
            filters.append(Ticket.answered == answered)
        # if 'label' in request.args:
        #     label_id = Label.query\
        #         .filter(Label.name == request.args['label']).one().id
        #     filters.append(Ticket.label_id == label_id)
        tickets = Ticket.query.filter(and_(*filters)).all()
        return jsonify(tickets)
