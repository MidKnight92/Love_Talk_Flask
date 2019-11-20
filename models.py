import datetime 
from peewee import *

from flask_login import UserMixin 

DATABASE = SqliteDatabase('users.sqlite')

class User(UserMixin, Model):
	username = CharField(unique=True)
	password = CharField(unique=True)
	email = CharField()
	age = IntegerField(default=18)
	bio = CharField()
	prefrence = CharField()
	gender = CharField()
	class Meta :
		database = DATABASE

class Message(Model):
	sender_user_id = ForeignKeyField(User, backref='messages')
	message_text = CharField()
	date = TimestampField()
	recipent_user_id = ForeignKeyField(User, backref='messages') 
	class Meta :
		database = DATABASE


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Message], safe=True)
	print('table created')
	DATABASE.close()








