import models 

from flask import request, jsonify, Blueprint
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict

messages = Blueprint('messages', 'messages')

@messages.route('/', methods=['GET'])
def test_message_controller():
	return "boooooooo"
	# This should query the messages that the user sent and received 
	# query = (Users
 #         .select(Messages, Users)
 #         .join(Users)
 #         .where(Messages.user_id == sender_user_id and Messages.user_id == recipient_user_id))