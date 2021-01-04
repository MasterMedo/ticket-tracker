from datetime import datetime
from dataclasses import dataclass

from models import db
from models.comment import Comment


@dataclass
class Ticket(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    submitter_id: int = db.Column(db.Integer, db.ForeignKey('user.id'),
                                  nullable=False)
    category_id: int = db.Column(db.Integer, db.ForeignKey('category.id'),
                                 nullable=False)
    timestamp: datetime = db.Column(db.DateTime, nullable=False,
                                    default=datetime.utcnow)
    answered: bool = db.Column(db.Boolean, nullable=False, default=False)
    censored: bool = db.Column(db.Boolean, nullable=False, default=False)
    locked: bool = db.Column(db.Boolean, nullable=False, default=False)
    hidden: bool = db.Column(db.Boolean, nullable=False, default=False)
    content: str = db.Column(db.Text, nullable=False)
    excerpt: str = db.Column(db.Text, nullable=False)
    title: str = db.Column(db.String(80), nullable=False)
    comments: Comment = db.relationship('Comment', backref='ticket')
    # file

    def __repr__(self):
        return f'<Ticket #{self.id}>'
