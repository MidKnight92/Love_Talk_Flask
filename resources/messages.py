import models 

from flask import request, jsonify, Blueprint
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict

messages = Blueprint('messages', 'messages')

@messages.route('/', methods=['GET'])
@login_required
def get_messages():
	try:
		messages_instances = models.Message.select().where(
			models.Message.recipient_user_id == current_user.id
		)
		messages_dict = [model_to_dict(message) for message in messages_instances]
		return jsonify(data=messages_dict, status={
			'code': 200,
			"message": "Success"
		}), 200
	except models.DoesNotExist:
		return jsonify(data={}, status={
			"code": 401,
			"message": "error"
		}), 401

@messages.route('/<recipient_user_id>', methods=['POST'])
@login_required
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
@messages.route('/<id>', methods=["Delete"])
@login_required
def delete_message(id):
	message_to_delete = models.Message.get_by_id(id)
	if message_to_delete.recipient_user_id != current_user.id:
		return jsonify(data="Forbidden", status={
			'code': 403,
			'message': "user can only delete their own message"
			}), 403
	else:
		message_text = message_to_delete.message_text
		message_to_delete.delete_instance()
		return jsonify(data='deleted successfully', status={
			'code': 200,
			"message": "{} deleted successfully".format(message_text)
		})
	

	# This should query the messages that the user sent and received 
	# query = (Users
 #         .select(Messages, Users)
 #         .join(Users)
 #         .where(Messages.user_id == sender_user_id and Messages.user_id == recipient_user_id))