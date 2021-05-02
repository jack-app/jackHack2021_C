from flask import jsonify

from models.user import User


def get_users():
    users = User.get_users()

    res = []
    for user in users:
        user_dict = user.to_dict()
        res.append(user_dict)
    return jsonify(res)
