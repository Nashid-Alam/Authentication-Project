import json
from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from api.users import users_bp


app = Flask(__name__)
app.register_blueprint(users_bp)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/login'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)    
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route('/', methods=['GET'])
def index():
    return Response('Hello World', status=200)


if __name__ == '__main__':
    
    app.run()
