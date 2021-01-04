from tests import BaseTestCase
from models import db
from schemas.comment import CommentSchema


class TestCommentSchema(BaseTestCase):
    def test_valid_post(self):
        json = {'content': 'This is a test.'}
        json.update({'submitter': self.dummy_user,
                     'ticket': self.dummy_ticket})
        schema = CommentSchema()
        comment = schema.load(json, session=db.session)
        db.session.add(comment)
        db.session.commit()
        assert comment.id is not None

    def test_valid_put(self):
        json = {'content': 'This is a test number 2.'}
        json.update({'ticket': self.dummy_ticket})
        schema = CommentSchema()
        comment = schema.load(json, instance=self.dummy_comment,
                              partial=True, session=db.session,)
        db.session.add(comment)
        db.session.commit()
        assert comment == self.dummy_comment
        assert comment.id == self.dummy_ticket.id
        assert comment.content == 'This is a test number 2.'
        assert comment.submitter == self.dummy_user
        assert comment.id is not None
