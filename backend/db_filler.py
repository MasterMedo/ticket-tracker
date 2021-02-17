from models.user import User
from models.ticket import Ticket
from models.comment import Comment
from models.label import Label
from models.category import Category
from models.accounttype import Accounttype
from app import db


accounttype_admin = Accounttype(name='admin')
accounttype_member = Accounttype(name='member')
accounttype_guest = Accounttype(name='guest')
accounttype_collaborator = Accounttype(name='collaborator')

user_mastermedo = User(username='mastermedo',
                       email='master.medo@gmail.com',
                       accounttype=accounttype_admin)

label_todo = Label(name='todo')  # task
label_bug = Label(name='bug')
label_enhancement = Label(name='enhancement')  # improvement
label_feature_request = Label(name='feature request')  # new feature

category_general = Category(name='general')
category_questions = Category(name='questions')
category_showcase = Category(name='showcase')

ticket1 = Ticket(title='First Ticket',
                 content='Is this even a ticket?',
                 excerpt='ticket 1',
                 submitter=user_mastermedo,
                 category=category_questions)
ticket2 = Ticket(title='Second Ticket',
                 content='Sample text for ticket 2!',
                 excerpt='Special excerpt!',
                 submitter=user_mastermedo,
                 category=category_general)
ticket3 = Ticket(title='Third Ticket',
                 content='Sample text for ticket 3!',
                 excerpt='Hidden excerpt!',
                 submitter=user_mastermedo,
                 category=category_showcase)

comment1 = Comment(content='first comment',
                   ticket=ticket1,
                   submitter=user_mastermedo)
comment2 = Comment(content='second comment',
                   ticket=ticket2,
                   submitter=user_mastermedo)
comment3 = Comment(content='third comment',
                   ticket=ticket1,
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
db.session.add(ticket1)
db.session.add(ticket2)
db.session.add(ticket3)
db.session.add(comment1)
db.session.add(comment2)
db.session.add(comment3)

db.session.commit()
