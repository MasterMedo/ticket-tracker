from tests import BaseTestCase
from models import db


class TestLabelModel(BaseTestCase):
    def test_valid_label_creation(self):
        db.session.add(self.dummy_label)
        db.session.commit()
