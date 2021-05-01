from flask import jsonify, request

from models.hello import Hello


def get_hello():
    hellos = Hello.getHello()
    print(hellos)

    return jsonify({"hello": "world"})


def post_hello():
    message = request.json["message"]
    Hello.postHello(message)

    return jsonify({"success": "Post"})
