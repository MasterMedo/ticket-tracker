from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from tests import BaseTestCase
from models import db
from schemas.user import UserSchema


class TestUserSchema(BaseTestCase):
    def test_valid_post(self):
        json = {'username': 'test', 'email': 'test.test@test.com'}
        json.update({'accounttype': self.dummy_accounttype})
        schema = UserSchema()
        user = schema.load(json, session=db.session)
        db.session.add(user)
        db.session.commit()

    def test_valid_put(self):
        json = {'username': 'test'}
        json.update({'accounttype': self.dummy_accounttype})
        schema = UserSchema()
        user = schema.load(json, instance=self.dummy_user,
                           partial=True, session=db.session)
        db.session.add(user)
        db.session.commit()

    def test_username_empty(self):
        with self.assertRaisesRegex(ValidationError, 'Length must be between'):
            json = {'username': '', 'email': 'test.test@test.com'}
            json.update({'accounttype': self.dummy_accounttype})
            user = UserSchema().load(json, session=db.session)
            db.session.add(user)
            db.session.commit()

    def test_missing_username(self):
        error_message = 'Missing data for required field.'
        with self.assertRaisesRegex(ValidationError, error_message):
            json = {'email': 'test.test@test.com'}
            json.update({'accounttype': self.dummy_accounttype})
            user = UserSchema().load(json, session=db.session)
            db.session.add(user)
            db.session.commit()

    def test_invalid_username(self):
        error_message = 'String does not match expected pattern.'
        with self.assertRaisesRegex(ValidationError, error_message):
            json = {'username': 'U$$39name', 'email': 'test.test@test.com'}
            json.update({'accounttype': self.dummy_accounttype})
            user = UserSchema().load(json, session=db.session)
            db.session.add(user)
            db.session.commit()

    def test_existing_username_capitalised(self):
        error_message = 'UNIQUE'
        with self.assertRaisesRegex(IntegrityError, error_message):
            json = {'username': 'UsERnaMe', 'email': 'test@test.com'}
            json.update({'accounttype': self.dummy_accounttype})
            json2 = {'username': 'username', 'email': 'test.test@test.com'}
            json2.update({'accounttype': self.dummy_accounttype})
            user = UserSchema().load(json, session=db.session)
            user2 = UserSchema().load(json2, session=db.session)
            db.session.add(user)
            db.session.add(user2)
            db.session.commit()

    def test_missing_email(self):
        error_message = 'Missing data for required field.'
        with self.assertRaisesRegex(ValidationError, error_message):
            json = {'username': 'test'}
            json.update({'accounttype': self.dummy_accounttype})
            user = UserSchema().load(json, session=db.session)
            db.session.add(user)
            db.session.commit()

    def test_invalid_email(self):
        error_message = 'Not a valid email address.'
        with self.assertRaisesRegex(ValidationError, error_message):
            json = {'username': 'user', 'email': 'test.test.com'}
            json.update({'accounttype': self.dummy_accounttype})
            user = UserSchema().load(json, session=db.session)
            db.session.add(user)
            db.session.commit()

    def test_missing_accounttype(self):
        error_message = 'Missing data for required field.'
        with self.assertRaisesRegex(ValidationError, error_message):
            json = {'username': 'test', 'email': 'test@test.com'}
            user = UserSchema().load(json, session=db.session)
            db.session.add(user)
            db.session.commit()
