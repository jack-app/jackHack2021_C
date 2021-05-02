from flask import jsonify, request

from models.hello import Hello


def get_hello():
    hellos = Hello.getHello()

    res = []
    for h in hellos:
        h_dict = h.to_dict()
        res.append(h_dict)

    return jsonify(res)


def post_hello():
    message = request.json["message"]
    Hello.postHello(message)

    return jsonify({"success": "Post"})
