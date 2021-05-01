from flask import jsonify

from models.hello import Hello


def hello():
    hellos = Hello.getHello()
    print(hellos)

    return jsonify({"hello": "world"})
