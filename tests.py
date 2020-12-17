import unittest
from flask import Flask
from models import db, Comment, Category, User, Post, Label
from sqlalchemy.exc import IntegrityError


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.app = app
        db.init_app(app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestUserModel(BaseTestCase):
    def test_valid_user_creation(self):
        user = User(username='test_user', email='test_email@test.com')
        db.session.add(user)
        assert user.posts == []
        db.session.commit()

    def test_no_email(self):
        with self.assertRaisesRegex(IntegrityError, 'NOT NULL constraint failed: user.email'):
            user = User(username='test_user')
            db.session.add(user)
            db.session.commit()

    def test_no_username(self):
        with self.assertRaisesRegex(IntegrityError, 'NOT NULL constraint failed: user.username'):
            user = User(email='test_email@test.com')
            db.session.add(user)
            db.session.commit()

    def test_username_already_exists(self):
        with self.assertRaisesRegex(IntegrityError, 'UNIQUE constraint failed: user.username'):
            user1 = User(username='test', email='test_email_1@test.com')
            user2 = User(username='test', email='test_email_2@test.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

    def test_email_already_exists(self):
        with self.assertRaisesRegex(IntegrityError, 'UNIQUE constraint failed: user.email'):
            user1 = User(username='test_1', email='test_email@test.com')
            user2 = User(username='test_2', email='test_email@test.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()


if __name__ == '__main__':
    unittest.main()
