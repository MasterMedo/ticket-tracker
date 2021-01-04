from dataclasses import dataclass
from models import db
from models.ticket import Ticket


@dataclass
class Category(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    tickets: Ticket = db.relationship('Ticket', backref='category')

    def __repr__(self):
        return f'<Category #{self.name}>'
