from dataclasses import dataclass
from models import db, ticket_label
from models.ticket import Ticket


@dataclass
class Label(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    tickets: Ticket = db.relationship('Ticket', secondary=ticket_label,
                                      backref='labels', lazy=True)

    def __repr__(self):
        return f'<Label {self.name}>'
