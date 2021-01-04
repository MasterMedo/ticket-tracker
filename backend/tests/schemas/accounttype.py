from marshmallow import ValidationError

from tests import BaseTestCase
from models import db
from schemas.accounttype import AccounttypeSchema


class TestAccounttypeSchema(BaseTestCase):
    def test_valid_post(self):
        json = {'name': 'admin'}
        schema = AccounttypeSchema()
        accounttype = schema.load(json, session=db.session)
        db.session.add(accounttype)
        db.session.commit()

    def test_valid_put(self):
        json = {'name': 'admin'}
        schema = AccounttypeSchema()
        accounttype = schema.load(json, instance=self.dummy_accounttype,
                                  partial=True, session=db.session)
        db.session.add(accounttype)
        db.session.commit()

    def test_name_empty(self):
        with self.assertRaisesRegex(ValidationError, 'Length must be between'):
            json = {'name': ''}
            schema = AccounttypeSchema()
            accounttype = schema.load(json, session=db.session)
            db.session.add(accounttype)
            db.session.commit()
