from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from resources.users import users
from resources.messages import messages

import models 

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = "this is a super secret"

#CORS 
# it's also a way that servers can say -- here's who I'm expecting to hear from, to only let certain origins communicate with that server (security)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(messages, origins=['http://localhost:3000'], supports_credentials=True)
# supports_credentials=True -- lets us take requests with cookies attached
# so we can use sessions

app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(messages, url_prefix='/api/v1/messages')

@app.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response


login_manager = LoginManager()

login_manager.init_app(app)


# This sets the callback for reloading a user from the session. The function you set should take a user ID (a unicode) and return a user object, or None if the user does not exist.
@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(data={
		'error': 'User not logged in'
		}, status={
		'code': 401,
		'message': 'You must have an account to do that'
		}), 401

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
