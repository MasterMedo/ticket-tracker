from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

ticket_label = db.Table('ticket_label', db.Model.metadata,
                        db.Column('ticket_id',
                                  db.Integer,
                                  db.ForeignKey('ticket.id')),
                        db.Column('label_id',
                                  db.Integer,
                                  db.ForeignKey('label.id')))
