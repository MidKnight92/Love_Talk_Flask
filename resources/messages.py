import models 

from flask import request, jsonify, Blueprint
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict

messages = Blueprint('messages', 'messages')

@messages.route('/', methods=['GET'])
def test_message_controller():
	return "boooooooo"