import models 

from flask import request, jsonify, Blueprint
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict

messages = Blueprint('messages', 'messages')

@messages.route('/', methods=['GET'])
def test_message_controller():
	return "boooooooo"

@messages.route('/<recipient_user_id>', methods=['POST'])
#@login_required
def create_message(recipient_user_id):
	payload = request.get_json()
	message = models.Message.create(message_text=payload['message_text'],
		sender_user = current_user.id,
		recipient_user = recipient_user_id)
	message_model = model_to_dict(message)
	return jsonify(data=message_model, status={
		'code': 201,
		'message': 'Message was successfully created'
		}), 201


	# This should query the messages that the user sent and received 
	# query = (Users
 #         .select(Messages, Users)
 #         .join(Users)
 #         .where(Messages.user_id == sender_user_id and Messages.user_id == recipient_user_id))