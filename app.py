from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from resources.users import users
from resources.messages import messages

import models 

DEBUG = True
PORT = 8000

app = Flask(__name__)

#CORS 
# it's also a way that servers can say -- here's who I'm expecting to hear from, to only let certain origins communicate with that server (security)
CORS(users, origins=['http://localhost:3000'], support_credentials=True)
CORS(messages, origins=['http://localhost:3000'], support_credentials=True)
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

# --------------- NEED THIS LATER --
# login_manager = LoginManager()

# login_manager.init_app(app)


# This sets the callback for reloading a user from the session. The function you set should take a user ID (a unicode) and return a user object, or None if the user does not exist.
# @login_manager.user_loader
# def load_user(userId):
	#return jsonify(data=)


# ------ ^ NEED THIS LATER  ^ ----

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
