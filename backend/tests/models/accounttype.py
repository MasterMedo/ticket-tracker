from tests import BaseTestCase
from models import db


class TestAccounttypeModel(BaseTestCase):
    def test_valid_accounttype_creation(self):
        db.session.add(self.dummy_accounttype)
        db.session.commit()
