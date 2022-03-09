from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    messages = db.relationship('Message')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    dept = db.Column(db.String(6))
    chats = db.relationship('Chat')
