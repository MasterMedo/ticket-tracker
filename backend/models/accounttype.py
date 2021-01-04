from dataclasses import dataclass
from models import db
from models.user import User


@dataclass
class Accounttype(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    users: User = db.relationship('User', backref='accounttype')

    def __repr__(self):
        return f'<Accounttype {self.name} #{self.id}>'
