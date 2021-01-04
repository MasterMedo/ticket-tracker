from flask import jsonify
from flask_restx import Resource

from api import api, model
from models import db
from models.comment import Comment
from models.ticket import Ticket
from models.user import User
from schemas.comment import CommentSchema


@api.route('/comments/<int:id>')
class CommentController(Resource):
    def get(self, id):
        """ Get comment by id """
        comment = Comment().query.get(id)
        return jsonify(comment)

    def delete(self, id):
        """ Delete comment by id """
        comment = Comment().query.get(id)
        db.session.delete(comment)
        db.session.commit()
        return jsonify(comment)

    @api.expect(model)
    def put(self, id):
        """ Edit comment by id """
        comment = Comment().query.get(id)
        schema = CommentSchema()
        comment = schema.load(api.payload, instance=comment, partial=True,
                              session=db.session)
        db.session.add(comment)
        db.session.commit()
        return jsonify(comment)


@api.route('/comments/<int:ticket_id>/comment')
class CommentControllerNew(Resource):
    @api.expect(model)
    def ticket(self, ticket_id):
        """ Create a new comment. """
        mock_user = User.query.first()
        ticket = Ticket().query.get(ticket_id)
        api.payload.update({'submitter': mock_user, 'ticket': ticket})
        comment = CommentSchema().load(api.payload, session=db.session)
        db.session.add(comment)
        db.session.commit()
        return jsonify(comment)
