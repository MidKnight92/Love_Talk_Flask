import models 

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def list_users():
	return "heeyyyyyyyyyy"

# POST(ing data) user is registering
@users.route('/register', methods=['POST'])
def register():
	# payload = request.get_json()
	return "register"
	# You can also add a person by calling the create() method, which returns a model instance:

# POST(ing data) USER IS LOGGING IN
@users.route('/login', methods=['POST'])
def login():
	return 'login'

# EDIT USERS PROFILE
@users.route('/', methods=['PUT'])
def update_user():
	return 'EDIT'
	# To update a row, modify the model instance and call save() to persist the changes. Here we will change Grandma’s name and then save the changes in the database:

#USERS LOGOUT
@users.route('/logout', methods=['GET'])
def logout():
	return 'logout'

# Delete Users Account
@users.route('/', methods=['Delete'])
def delete_account():
	return "you deleted me"
	# The return value of delete_instance() is the number of rows removed from the database.

