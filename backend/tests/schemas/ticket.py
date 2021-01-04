from tests import BaseTestCase
from models import db
from schemas.ticket import TicketSchema


class TestTicketSchema(BaseTestCase):
    def test_valid_post(self):
        json = {'title': 'test', 'content': 'This is a test.'}
        json.update({'submitter': self.dummy_user,
                     'category': self.dummy_category})
        schema = TicketSchema()
        ticket = schema.load(json, session=db.session)
        db.session.add(ticket)
        db.session.commit()
        assert ticket.excerpt == ticket.content
        assert ticket.id is not None

    def test_valid_put(self):
        json = {'title': 'test', 'content': 'This is a test number 2.'}
        json.update({'category': self.dummy_category})
        schema = TicketSchema()
        ticket = schema.load(json, instance=self.dummy_ticket,
                             partial=True, session=db.session,)
        db.session.add(ticket)
        db.session.commit()
        assert ticket == self.dummy_ticket
        assert ticket.id == self.dummy_ticket.id
        assert ticket.title == 'Test'
        assert ticket.content == 'This is a test number 2.'
        assert ticket.submitter == self.dummy_user
        assert ticket.id is not None

    def test_valid_ticket_with_labels(self):
        json = {'title': 'test', 'content': 'This is a test.'}
        json.update({'submitter': self.dummy_user,
                     'category': self.dummy_category,
                     'labels': [self.dummy_label]})
        schema = TicketSchema()
        ticket = schema.load(json, session=db.session)
        db.session.add(ticket)
        db.session.commit()
        assert ticket.excerpt == ticket.content
        assert ticket.labels == [self.dummy_label]
        assert ticket.id is not None
