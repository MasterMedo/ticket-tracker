from models import User, Accounttype, Post, Comment, Category, Label
from app import db


accounttype_admin = Accounttype(name='admin')
accounttype_member = Accounttype(name='member')
accounttype_guest = Accounttype(name='guest')
accounttype_collaborator = Accounttype(name='collaborator')

user_mastermedo = User(username='mastermedo',
                       email='master.medo@gmail.com',
                       accounttype=accounttype_admin)

label_todo = Label(name='todo')
label_bug = Label(name='bug')
label_enhancement = Label(name='enhancement')
label_feature_request = Label(name='feature request')

category_general = Category(name='general')
category_questions = Category(name='questions')
category_showcase = Category(name='showcase')

post1 = Post(title='First Post',
             content='Is this even a ticket?',
             excerpt='post 1',
             submitter=user_mastermedo,
             category=category_questions)
post2 = Post(title='Second Post',
             content='Sample text for post 2!',
             excerpt='Special excerpt!',
             submitter=user_mastermedo,
             category=category_general)
post3 = Post(title='Third Post',
             content='Sample text for post 3!',
             excerpt='Hidden excerpt!',
             submitter=user_mastermedo,
             category=category_showcase)

comment1 = Comment(content='first comment',
                   post=post1,
                   submitter=user_mastermedo)
comment2 = Comment(content='second comment',
                   post=post2,
                   submitter=user_mastermedo)
comment3 = Comment(content='third comment',
                   post=post1,
                   submitter=user_mastermedo)

db.create_all()

db.session.add(accounttype_admin)
db.session.add(accounttype_member)
db.session.add(accounttype_guest)
db.session.add(accounttype_collaborator)
db.session.add(user_mastermedo)
db.session.add(label_todo)
db.session.add(label_bug)
db.session.add(label_enhancement)
db.session.add(label_feature_request)
db.session.add(category_questions)
db.session.add(category_general)
db.session.add(category_showcase)
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(comment1)
db.session.add(comment2)
db.session.add(comment3)

db.session.commit()
