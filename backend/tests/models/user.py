from sqlalchemy.exc import IntegrityError

from tests import BaseTestCase
from models import db
from models.user import User


class TestUserModel(BaseTestCase):
    def test_valid_user_creation(self):
        db.session.add(self.dummy_user)
        db.session.commit()

    def test_no_email(self):
        with self.assertRaisesRegex(IntegrityError,
                                    'NOT NULL constraint failed: user.email'):
            user = User(username='test_user',
                        accounttype=self.dummy_accounttype)
            db.session.add(user)
            db.session.commit()

    def test_no_accounttype(self):
        error_message = 'NOT NULL constraint failed: user.accounttype'
        with self.assertRaisesRegex(IntegrityError, error_message):
            user = User(username='test_user', email='test@test.com')
            db.session.add(user)
            db.session.commit()

    def test_no_username(self):
        error_message = 'NOT NULL constraint failed: user.username'
        with self.assertRaisesRegex(IntegrityError, error_message):
            user = User(email='test_email@test.com',
                        accounttype=self.dummy_accounttype)
            db.session.add(user)
            db.session.commit()

    def test_username_already_exists(self):
        with self.assertRaisesRegex(IntegrityError,
                                    'UNIQUE constraint failed: user.username'):
            user1 = User(username='test', email='test_email_1@test.com',
                         accounttype=self.dummy_accounttype)
            user2 = User(username='test', email='test_email_2@test.com',
                         accounttype=self.dummy_accounttype)
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

    def test_email_already_exists(self):
        with self.assertRaisesRegex(IntegrityError,
                                    'UNIQUE constraint failed: user.email'):
            user1 = User(username='test_1', email='test_email@test.com',
                         accounttype=self.dummy_accounttype)
            user2 = User(username='test_2', email='test_email@test.com',
                         accounttype=self.dummy_accounttype)
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
