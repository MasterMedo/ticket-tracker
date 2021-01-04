from marshmallow import fields, validate, pre_load
from models.accounttype import Accounttype
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class AccounttypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Accounttype
        load_instance = True

    name = fields.String(validate=validate.Length(1, 50))

    @pre_load
    def lowercase_username(self, data, **kwargs):
        if 'name' in data:
            data['name'] = data['name'].lower()
        return data
