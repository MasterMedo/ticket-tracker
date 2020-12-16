from flask import Flask, jsonify
from flask.json import JSONEncoder
from models import db, User, Post, Comment, Accounttype, Label, Category
from datetime import datetime, timedelta
from flask_restx import Resource, Api
from collections import defaultdict
from schemas import CommentSchema, UserSchema
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == timedelta:
            return str(o)
        elif type(o) == datetime:
            return o.isoformat()
        else:
            return super().default(o)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test11.db'
app.json_encoder = CustomJSONEncoder
db.app = app
db.init_app(app)
ma = Marshmallow(app)
api = Api(app, version='0.1', title='Tickets Api',
          description='Api for the Tickets app.')

model = api.model('', defaultdict())


@api.route('/users/<username>')
class UserController(Resource):
    def get(self, username):
        """ Get user by username """
        user = db.session.query(User).filter(User.username == username).first()
        return jsonify(user)

    @api.expect(model)
    def put(self, username):
        """ Edit user by username """
        user = db.session.query(User).filter(User.username == username).first()
        schema = UserSchema()
        user = schema.load(api.payload, instance=user, partial=True,
                           session=db.session)
        db.session.add(user)
        db.session.commit()
        return jsonify(user)


@api.route('/register/<accounttype>')
class UserControllerNew(Resource):
    @api.expect(model)
    def post(self, accounttype):
        """ Create <accounttype> user """
        acctype = db.session.query(Accounttype)\
                            .filter(Accounttype.name == accounttype).first()
        if acctype is None:
            raise ValidationError(f"Accounttype `{accounttype}` doesn't exist")

        user = UserSchema().load(api.payload, session=db.session)
        user.accounttype = acctype
        db.session.add(user)
        db.session.commit()
        return jsonify(user)


@api.route('/labels/<int:id>')
class LabelController(Resource):
    def get(self, id):
        """ Get label by id """
        label = db.session.query(Label).filter(Label.id == id).first()
        return jsonify(label)


@api.route('/posts/<int:id>')
class PostController(Resource):
    def get(self, id):
        """ Get post by id """
        post = db.session.query(Post).filter(Post.id == id).first()
        return jsonify(post)


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


@api.route('/comments/<int:post_id>/comment')
class CommentControllerNew(Resource):
    @api.expect(model)
    def post(self, post_id):
        """ Create a new comment. """
        comment = CommentSchema().load(api.payload, session=db.session)
        comment.post = Post().query.get(post_id)
        db.session.add(comment)
        db.session.commit()
        return jsonify(comment)


@api.route('/accounttypes/<int:accounttype_id>')
class AccounttypeController(Resource):
    def get(self, accounttype_id):
        """ Get account type by accounttype_id """
        accounttype = db.session.query(Accounttype).filter(Accounttype.id == accounttype_id).first()
        return jsonify(accounttype)


@api.route('/categories/<int:category_id>')
class CategoryController(Resource):
    def get(self, category_id):
        """ Get category by category_id """
        category = db.session.query(Category).filter(Category.id == category_id).first()
        return jsonify(category)


if __name__ == '__main__':
    app.run(debug=True)
