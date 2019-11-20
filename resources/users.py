import models 

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def list_users():
	return "heeyyyyyyyyyy"

# POST(ing data) user is registering
@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	payload['email'].lower()
	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify(data={}, status={'code': 401, "message": 
			"A user with that email already exist"}), 401
	except models.DoesNotExist:
		payload['password'] = generate_password_hash(payload['password'])
		user = models.User.create(**payload)
		login_user(user)
		user_dict = model_to_dict(user)
		print(user_dict)
		del user_dict['password']
		return jsonify(data=user_dict, status={'code': 201, 
			'message': 'Sucessfully registered {}'.format(user_dict(['email']))}),201
	# You can also add a person by calling the create() method, which returns a model instance:

# POST(ing data) USER IS LOGGING IN
@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	try:
		user = models.User.get(models.User.email == payload['email'])
		user_dict = model_to_dict(user)
		if(check_password_hash(user_dict['password'], payload['password'])):
			login_user(user)
			del user_dict['password']
			return jsonify(data=user_dict, status={'code': 200, 
				'message': "Sucessfully logged in {}".format(user_dict['email'])}), 200
		else: 
			print('password no good')
			return jsonify(data={}, status={'code': 401, 'message': 'Email or password id incorrect'}), 401
	except models.DoesNotExist:
		print('email not found')
		return jsonify(data={}, status={'code': 401, 'message': 'Email or password id incorrect'}), 401

# EDIT USERS PROFILE
@users.route('/', methods=['PUT'])
@login_required
def update_user():
	payload = request.get_json()
	# users = models.Users.get(models.User.id == current_user.id)
	print(model_to_dict(current_user))
	if(current_user.is_authenticated):
		current_user.bio = payload['bio'] if 'bio' in payload else None 
		current_user.save()
		user_dict = model_to_dict(current_user)
		user_dict.pop('password')
		return jsonify(data=user_dict, status={
			'code': 200,
			'message': 'Resource updated Sucessfully'
		}), 200
	else:
		return jsonify(data='Forbidden', status={
			'code': 403,
			'message': 'error'

		}), 403

	# To update a row, modify the model instance and call save() to persist the changes. Here we will change Grandma’s name and then save the changes in the database:

#USERS LOGOUT
@users.route('/logout', methods=['GET'])
def logout():
	email = model_to_dict(current_user)['email']
	logout_user()
	return jsonify(data={}, status={
		'code': 200,
		'message': "Sucessfully logged out {}".format(email)
		})

# Delete Users Account
@users.route('/', methods=['Delete'])
@login_required
def delete_account():
	if(current_user.is_authenticated):
		username = current_user.username
		current_user.delete_instance()
		return jsonify(data='Sucessfully Deleted', status={
			'code': 200,
			"message": "{} Deleted Sucessfully".format(username)
			})
	else: 
		return jsonify(data="Forbidden", status={
			'code': 403,
			'message': "User can only delete there Account"
			}), 403


	
# The return value of delete_instance() is the number of rows removed from the database.

