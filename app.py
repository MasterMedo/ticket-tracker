from flask import Flask, jsonify, abort
from flask.json import JSONEncoder
from models import db, User, Post, Comment, Accounttype, Label, Category
from datetime import datetime, timedelta
from flask_restx import Resource, Api
from collections import defaultdict
from schemas import CommentSchema, UserSchema, PostSchema, AccounttypeSchema, LabelSchema, CategorySchema
from sqlalchemy.orm.exc import NoResultFound
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test12.db'
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
        user = User.query.filter(User.username == username).one()
        return jsonify(user)

    def delete(self, username):
        """ Delete user by username """
        user = User.query.filter(User.username == username).one()
        db.session.delete(user)
        db.session.commit()
        return jsonify(user)

    @api.expect(model)
    def put(self, username):
        """ Edit user by username """
        user = User.query.filter(User.username == username).one()
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
        accounttype = Accounttype.query\
                                 .filter(Accounttype.name == accounttype).one()
        api.payload['accounttype'] = accounttype
        user = UserSchema().load(api.payload, session=db.session)
        db.session.add(user)
        db.session.commit()
        return jsonify(user)


@api.route('/labels/<int:id>')
class LabelController(Resource):
    def get(self, id):
        """ Get label by id """
        label = Label.query.filter(Label.id == id).one()
        return jsonify(label)

    def delete(self, id):
        """ Delete label by id """
        label = Label.query.filter(Label.id == id).one()
        db.session.delete(label)
        db.session.commit()
        return jsonify(label)

    @api.expect(model)
    def put(self, id):
        """ Edit label by id """
        label = Label.query.filter(Label.id == id).one()
        label = LabelSchema().load(api.payload, instance=label, partial=True,
                                   session=db.session)
        db.session.add(label)
        db.session.commit()
        return jsonify(label)


@api.route('/labels/')
class LabelControllerNew(Resource):
    @api.expect(model)
    def post(self):
        label = LabelSchema().load(api.payload, session=db.session)
        db.session.add(label)
        db.session.commit()
        return jsonify(label)


@api.route('/posts/<int:id>')
class PostController(Resource):
    def get(self, id):
        """ Get post by id """
        post = db.session.query(Post).filter(Post.id == id).one()
        return jsonify(post)

    def delete(self, id):
        """ delete post by id """
        post = db.session.query(Post).filter(Post.id == id).one()
        db.session.delete(post)
        db.session.commit()
        return jsonify(post)

    @api.expect(model)
    def put(self, id):
        post = db.session.query(Post).filter(Post.id == id).one()
        post = PostSchema().load(api.payload, instance=post, partial=True,
                                 session=db.session)
        db.session.add(post)
        db.session.commit()
        return jsonify(post)


@api.route('/posts/<category>')
class PostControllerNew(Resource):
    @api.expect(model)
    def post(self, category):
        mock_user = User.query.first()
        category = Category.query.filter(Category.name == category).one()
        api.payload.update({'submitter': mock_user, 'category': category})
        post = PostSchema().load(api.payload, session=db.session)
        category
        db.session.add(post)
        db.session.commit()
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
        mock_user = User.query.first()
        post = Post().query.get(post_id)
        api.payload.update({'submitter': mock_user, 'post': post})
        comment = CommentSchema().load(api.payload, session=db.session)
        db.session.add(comment)
        db.session.commit()
        return jsonify(comment)


@api.route('/accounttypes/<accounttype>')
class AccounttypeController(Resource):
    def get(self, accounttype):
        """ Get account type by account type name """
        accounttype = Accounttype.query\
                                 .filter(Accounttype.name == accounttype).one()
        return jsonify(accounttype)

    @api.expect(model)
    def put(self, accounttype):
        """ Edit account type by account type name """
        accounttype = Accounttype.query\
                                 .filter(Accounttype.name == accounttype).one()
        accounttype = AccounttypeSchema().load(api.payload, partial=True,
                                               session=db.session,
                                               instance=accounttype)
        db.session.add(accounttype)
        db.session.commit()
        return jsonify(accounttype)

    def delete(self, accounttype):
        """ Delete account type by account type name """
        accounttype = Accounttype.query\
                                 .filter(Accounttype.name == accounttype).one()
        db.session.delete(accounttype)
        db.session.commit()
        return jsonify(accounttype)


@api.route('/accounttypes/')
class AccounttypeControllerNew(Resource):
    @api.expect(model)
    def post(self):
        accounttype = AccounttypeSchema().load(api.payload, session=db.session)
        db.session.add(accounttype)
        db.session.commit()
        return jsonify(accounttype)


@api.route('/categories/<int:category_id>')
class CategoryController(Resource):
    def get(self, category_id):
        """ Get category by category_id """
        category = Category.query.filter(Category.id == category_id).one()
        return jsonify(category)

    @api.expect(model)
    def put(self, category_id):
        """ Edit category by category_id """
        category = Category.query.filter(Category.id == category_id).one()
        category = CategorySchema().load(api.payload, session=db.session)
        db.session.add(category)
        db.session.commit()
        return jsonify(category)

    def delete(self, category_id):
        """ Delete category by category_id """
        category = Category.query.filter(Category.id == category_id).one()
        db.session.delete(category)
        db.session.commit()
        return jsonify(category)


@api.route('/categories/')
class CategoryControllerNew(Resource):
    @api.expect(model)
    def post(self):
        category = CategorySchema().load(api.payload, session=db.session)
        db.session.add(category)
        db.session.commit()
        return jsonify(category)


@api.errorhandler(NoResultFound)
def handle_no_result_exception(error):
    '''Return a custom not found error message and 404 status code'''
    return {'message': str(error)}, 404


if __name__ == '__main__':
    app.run(debug=True)
