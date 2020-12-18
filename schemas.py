from marshmallow import ValidationError, validates, post_load, fields, validate, pre_load
from models import db, Comment, Post, User, Accounttype, Label, Category
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field, fields as dbfields


class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True

    submitter = fields.Raw(required=True)
    post = fields.Raw(required=True)

    @validates('submitter')
    def validate_submitter(self, submitter):
        if not isinstance(submitter, User):
            raise ValidationError('Wrong type for field.')

    @validates('post')
    def validate_post(self, post):
        if not isinstance(post, Post):
            raise ValidationError('Wrong type for field.')

    @pre_load
    def strip_content(self, data, **kwargs):
        if 'content' in data:
            data['content'] = data['content'].strip()
        return data


class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
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
