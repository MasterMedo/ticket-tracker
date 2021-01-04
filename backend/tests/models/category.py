from tests import BaseTestCase
from models import db


class TestCategoryModel(BaseTestCase):
    def test_valid_category_creation(self):
        db.session.add(self.dummy_category)
        db.session.commit()
