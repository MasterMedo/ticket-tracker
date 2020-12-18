import unittest
from flask import Flask
from models import db, Comment, Category, User, Post, Label, Accounttype
from schemas import CommentSchema, CategorySchema, UserSchema, PostSchema, LabelSchema, AccounttypeSchema
from marshmallow import ValidationError
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
        self.dummy_accounttype = Accounttype(name='dummy')
        self.dummy_category = Category(name='dummy')
        self.dummy_label = Label(name='dummy')
        self.dummy_user = User(username='dummy', email='dummy@dummy.com',
                               accounttype=self.dummy_accounttype)
        self.dummy_post = Post(content='dummy', title='dummy', excerpt='dummy',
                               category=self.dummy_category,
                               submitter=self.dummy_user)
        self.dummy_comment = Comment(content='dummy', post=self.dummy_post,
                                     submitter=self.dummy_user)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCommentModel(BaseTestCase):
    def test_valid_comment_creation(self):
        db.session.add(self.dummy_comment)
        db.session.commit()


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


class TestAccounttypeModel(BaseTestCase):
    def test_valid_accounttype_creation(self):
        db.session.add(self.dummy_accounttype)
        db.session.commit()


class TestLabelModel(BaseTestCase):
    def test_valid_label_creation(self):
        db.session.add(self.dummy_label)
        db.session.commit()


class TestCategoryModel(BaseTestCase):
    def test_valid_category_creation(self):
        db.session.add(self.dummy_category)
        db.session.commit()


class TestPostModel(BaseTestCase):
    def test_valid_post_creation(self):
        db.session.add(self.dummy_post)
        db.session.commit()


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


class TestUserSchema(BaseTestCase):
    def test_valid_post(self):
        json = {'username': 'test', 'email': 'test.test@test.com'}
        json.update({'accounttype': self.dummy_accounttype})
        schema = UserSchema()
        user = schema.load(json, session=db.session)
        db.session.add(user)
        db.session.commit()

    def test_valid_put(self):
        json = {'username': 'test', 'email': 'test.test@test.com'}
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


if __name__ == '__main__':
    unittest.main()
