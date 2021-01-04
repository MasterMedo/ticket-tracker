from tests import BaseTestCase
from models import db


class TestTicketModel(BaseTestCase):
    def test_valid_ticket_creation(self):
        db.session.add(self.dummy_ticket)
        db.session.commit()
