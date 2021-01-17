from dataclasses import dataclass

from models import db
from models.ticket import Ticket
from models.comment import Comment


@dataclass
class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(30), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)

    tickets: Ticket = db.relationship('Ticket', backref='submitter')
    comments: Comment = db.relationship('Comment', backref='submitter')
    accounttype_id: int = db.Column(db.Integer,
                                    db.ForeignKey('accounttype.id'),
                                    nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
