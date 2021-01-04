from marshmallow import ValidationError, validates, fields, pre_load
from models.comment import Comment
from models.ticket import Ticket
from models.user import User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True

    submitter = fields.Raw(required=True)
    ticket = fields.Raw(required=True)

    @validates('submitter')
    def validate_submitter(self, submitter):
        if not isinstance(submitter, User):
            raise ValidationError('Wrong type for field.')

    @validates('ticket')
    def validate_ticket(self, ticket):
        if not isinstance(ticket, Ticket):
            raise ValidationError('Wrong type for field.')

    @pre_load
    def strip_content(self, data, **kwargs):
        if 'content' in data:
            data['content'] = data['content'].strip()
        return data
