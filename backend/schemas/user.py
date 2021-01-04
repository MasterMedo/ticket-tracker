from marshmallow import ValidationError, validates, fields, validate, pre_load
from models.user import User
from models.accounttype import Accounttype
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    username = fields.String(validate=[validate.Length(1, 30),
                                       validate.Regexp(r'^\w+$')],
                             required=True)
    email = fields.Email(required=True, validate=validate.Length(1, 120))
    accounttype = fields.Raw(required=True)

    @validates('accounttype')
    def validate_category(self, accounttype):
        if not isinstance(accounttype, Accounttype):
            raise ValidationError('Wrong type for field.')

    @pre_load
    def lowercase_username(self, data, **kwargs):
        if 'username' in data:
            data['username'] = data['username'].lower()
        return data
