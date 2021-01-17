from flask import jsonify
from flask_restx import Resource

from api import api, model
from models import db
from models.category import Category
from schemas.category import CategorySchema


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

    def get(self):
        """ Get all categories """
        categories = Category.query.all()
        print(categories)
        return jsonify(categories)
