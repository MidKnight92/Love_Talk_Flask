from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from resources.users import users
from resources.messages import messages

import models 

DEBUG = True
PORT = 8000

app = Flask(__name__)

CORS(users, origins=['http://localhost:3000'], support_credentials=True)
CORS(messages, origins=['http://localhost:3000'], support_credentials=True)

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




if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
