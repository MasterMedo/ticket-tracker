from marshmallow import ValidationError, fields, validates, post_load
from models import db, Comment, Post, User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
