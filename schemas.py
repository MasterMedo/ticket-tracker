from marshmallow import ValidationError, validates, post_load, fields, validate, pre_load
from models import db, Comment, Post, User, Accounttype, Label, Category
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field, fields as dbfields


class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True


class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True


class AccounttypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Accounttype
        load_instance = True

    name = fields.String(validate=validate.Length(1, 50))


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    username = fields.String(validate=[validate.Length(1, 30),
                                       validate.Regexp(r'^\w+$')],
                             required=True)
    email = fields.Email(required=True, validate=validate.Length(1, 120))
    accounttype = fields.Raw(required=True)

    @pre_load
    def lowercase_username(self, data, **kwargs):
        if 'username' in data:
            data['username'] = data['username'].lower()
        return data


class LabelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Label
        load_instance = True

    name = fields.String(validate=validate.Length(1, 50), required=True)


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True

    name = fields.String(validate=validate.Length(1, 50))
