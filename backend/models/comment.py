from dataclasses import dataclass

from models import db


@dataclass
class Comment(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    ticket_id: int = db.Column(db.Integer, db.ForeignKey('ticket.id'),
                               nullable=False)
    submitter_id: int = db.Column(db.Integer, db.ForeignKey('user.id'),
                                  nullable=False)
    censored: bool = db.Column(db.Boolean, nullable=False, default=False)
    content: str = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Comment #{self.id}>'
