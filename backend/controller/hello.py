from flask import jsonify


def hello():
    return jsonify({"hello": "world"})
