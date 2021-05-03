from flask import jsonify, request, abort

from models.user import User
from utils.check_params import check_params


def get_users():
    users = User.get_users()

    res = []
    for user in users:
        user_dict = user.to_dict()
        res.append(user_dict)
    return jsonify(res)


def get_user(user_id):
    user = User.get_user(user_id)

    return jsonify(user.to_dict())


def register_user():
    user_requests = ['name']

    if not check_params(request.json, user_requests):
        abort(400, {'message': 'parameter not found'})

    name = request.json["name"]

    if name == '':
        abort(400, {'message': 'name is null'})

    new_user = User(name=name)
    user_id = new_user.post_user()

    return jsonify({"id": user_id})
