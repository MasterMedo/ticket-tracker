from marshmallow import ValidationError
from tests import BaseTestCase
from models import db
from schemas.label import LabelSchema


class TestLabelSchema(BaseTestCase):
    def test_valid_post(self):
        json = {'name': 'questions'}
        schema = LabelSchema()
        label = schema.load(json, session=db.session)
        db.session.add(label)
        db.session.commit()

    def test_valid_put(self):
        json = {'name': 'questions'}
        schema = LabelSchema()
        label = schema.load(json, instance=self.dummy_label,
                            partial=True, session=db.session)
        db.session.add(label)
        db.session.commit()

    def test_name_empty(self):
        with self.assertRaisesRegex(ValidationError, 'Length must be between'):
            json = {'name': ''}
            schema = LabelSchema()
            label = schema.load(json, session=db.session)
            db.session.add(label)
            db.session.commit()
