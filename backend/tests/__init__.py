import unittest
from flask import Flask
from models import db
from models.comment import Comment
from models.category import Category
from models.user import User
from models.ticket import Ticket
from models.label import Label
from models.accounttype import Accounttype


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
        self.dummy_user = User(username='dummy',
                               email='dummy@dummy.com',
                               accounttype=self.dummy_accounttype)
        self.dummy_ticket = Ticket(content='dummy',
                                   title='dummy',
                                   excerpt='dummy',
                                   category=self.dummy_category,
                                   submitter=self.dummy_user)
        self.dummy_comment = Comment(content='dummy',
                                     ticket=self.dummy_ticket,
                                     submitter=self.dummy_user)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
