import json
from flask import Blueprint, jsonify, request, Response


users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/', methods=['POST'])
def create_user():
    try:
        user = json.loads(request.data)
        username = user['username']
        password = user['password']
    except:
        return Response('Username or password not provided', status=400)
    else:
        if not username or not password:
            return Response('Username or password not provided', status=400)

    # if user.get('username') == None or user.get('username') == '':
    #     return Response('Username not provided', status=400)

    # if user.get('password') == None or user.get('password') == '':
    #     return Response('Password not provided', status=400)    

    return Response(json.dumps(user), status=200, content_type='application/json')


@users_bp.route('/', methods=['GET'])
def get_users():
    users = [
        "all the users",
        {},
    ]
    return Response(json.dumps(users), status=200, content_type='application/json')


@users_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):

    user = {
        "id": user_id,
        "data": "some user data"
    }
    return Response(json.dumps(user), status=200, content_type='application/json')


@users_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    
    return Response(f'User with id={user_id} was deleted', status=200)


@users_bp.route('/<user_id>', methods=['PATCH'])
def update_user(user_id):
    print(request.data)
    print(request.json)
    try:
        update = json.loads(request.data) 
        print(update)
        username = update['username']
        password = update['password']
    except:
        return Response('please enter username and password', status=400) 
    
    response_object = {
        "id": user_id,
        "updated": update
    }
    # return jsonify(response_object)
    
    return Response(json.dumps(response_object), status=200, content_type='application/json')
