from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from resources.user import Users, SingleUser
from models.db import db




app = Flask(__name__)
CORS(app)
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

api.add_resource(Users, '/users')
api.add_resource(SingleUser, '/users/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
