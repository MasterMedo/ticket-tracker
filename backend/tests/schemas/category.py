from marshmallow import ValidationError
from tests import BaseTestCase
from models import db
from schemas.category import CategorySchema


class TestCategorySchema(BaseTestCase):
    def test_valid_post(self):
        json = {'name': 'questions'}
        schema = CategorySchema()
        category = schema.load(json, session=db.session)
        db.session.add(category)
        db.session.commit()

    def test_valid_put(self):
        json = {'name': 'questions'}
        schema = CategorySchema()
        accounttype = schema.load(json, instance=self.dummy_category,
                                  partial=True, session=db.session)
        db.session.add(accounttype)
        db.session.commit()

    def test_name_empty(self):
        with self.assertRaisesRegex(ValidationError, 'Length must be between'):
            json = {'name': ''}
            schema = CategorySchema()
            category = schema.load(json, session=db.session)
            db.session.add(category)
            db.session.commit()
