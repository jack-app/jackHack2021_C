from flask import jsonify, request

from models.user import User


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
    name = request.json["name"]
    new_user = User(name=name)
    user_id = new_user.post_user()

    return jsonify({"id": user_id})
