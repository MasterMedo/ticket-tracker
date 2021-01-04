from marshmallow import ValidationError, validates, fields, validate, pre_load
from models.ticket import Ticket
from models.user import User
from models.label import Label
from models.category import Category
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class TicketSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket
        load_instance = True

    title = fields.String(validate=validate.Length(1, 120), required=True)
    content = fields.String(validate=validate.Length(1, 65536), required=True)
    excerpt = fields.String(validate=validate.Length(1, 120), required=False)
    submitter = fields.Raw(required=True)
    category = fields.Raw(required=True)
    labels = fields.Raw(required=False)

    @validates('labels')
    def validate_labels(self, labels):
        if not isinstance(labels, list)\
                or any(not isinstance(label, Label) for label in labels):
            raise ValidationError('Wrong type for field.')

    @validates('submitter')
    def validate_submitter(self, submitter):
        if not isinstance(submitter, User):
            raise ValidationError('Wrong type for field.')

    @validates('category')
    def validate_category(self, category):
        if not isinstance(category, Category):
            raise ValidationError('Wrong type for field.')

    @pre_load
    def preprocess(self, data, **kwargs):
        if 'content' in data:
            data['content'] = data['content'].strip()

            if 'excerpt' not in data:
                data['excerpt'] = data['content'].split('\n')[0].strip()[:120]

        if 'title' in data:
            data['title'] = data['title'].strip().capitalize()

        return data
