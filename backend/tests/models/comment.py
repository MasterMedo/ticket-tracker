from tests import BaseTestCase
from models import db


class TestCommentModel(BaseTestCase):
    def test_valid_comment_creation(self):
        db.session.add(self.dummy_comment)
        db.session.commit()
