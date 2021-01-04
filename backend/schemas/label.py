from marshmallow import fields, validate, pre_load
from models.label import Label
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class LabelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Label
        load_instance = True

    name = fields.String(validate=validate.Length(1, 50), required=True)

    @pre_load
    def lowercase_username(self, data, **kwargs):
        if 'name' in data:
            data['name'] = data['name'].lower()
        return data
