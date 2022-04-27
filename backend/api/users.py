import json
from flask import Blueprint, request, Response

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/', methods=['POST'])
def create_user():
    user = json.loads(request.data)

    print(user)
    # if db.session.query(User) != '':
    #     data = User(username, password)
    #     db.session.add(data)
    #     # db.session.commit()

    return Response(json.dumps(user), status=200, content_type='application/json')


@users_bp.route('/', methods=['GET'])
def get_users():
    users = ['all the users data here']
    return Response(json.dumps(users), status=200, content_type='application/json')


@users_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = 'some user data'
    return Response(json.dumps(user), status=200, content_type='application/json')


@users_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    
    return Response(json.dumps('user deleted'), status=200, content_type='application/json')

