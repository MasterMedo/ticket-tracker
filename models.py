from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dataclasses import dataclass

db = SQLAlchemy()


@dataclass
class Comment(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    post_id: int = db.Column(db.Integer, db.ForeignKey('post.id'))
    censored: bool = db.Column(db.Boolean, nullable=False, default=False)
    content: str = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Comment #{self.id}>'


@dataclass
class Post(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id: int = db.Column(db.Integer, db.ForeignKey('category.id'))
    timestamp: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    answered: bool = db.Column(db.Boolean, nullable=False, default=False)
    censored: bool = db.Column(db.Boolean, nullable=False, default=False)
    locked: bool = db.Column(db.Boolean, nullable=False, default=False)
    hidden: bool = db.Column(db.Boolean, nullable=False, default=False)
    content: str = db.Column(db.Text, nullable=False)
    excerpt: str = db.Column(db.Text, nullable=False)
    title: str = db.Column(db.String(80), nullable=False)
    comments: Comment = db.relationship('Comment', backref='post')
    # file

    def __repr__(self):
        return f'<Post #{self.id}>'


@dataclass
class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(30), unique=True)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    posts: Post = db.relationship('Post', backref='user')
    accounttype_id: int = db.Column(db.Integer, db.ForeignKey('accounttype.id'))

    def __repr__(self):
        return f'<User {self.username}>'


@dataclass
class Accounttype(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    users: User = db.relationship('User', backref='accounttype')

    def __repr__(self):
        return f'<Accounttype {self.name} #{self.id}>'


post_label = db.Table('post_label', db.Model.metadata,
                      db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                      db.Column('label_id', db.Integer, db.ForeignKey('label.id')))


@dataclass
class Label(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    posts: Post = db.relationship('Post', secondary=post_label,
                                  backref='labels', lazy=True)

    def __repr__(self):
        return f'<Label {self.name}>'


@dataclass
class Category(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    posts: Post = db.relationship('Post', backref='category')

    def __repr__(self):
        return f'<Category #{self.name}>'
