from marshmallow import fields, validate, pre_load
from models.category import Category
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True

    name = fields.String(validate=validate.Length(1, 50))

    @pre_load
    def lowercase_username(self, data, **kwargs):
        if 'name' in data:
            data['name'] = data['name'].lower()
        return data
