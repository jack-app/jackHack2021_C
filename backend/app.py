import os

from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.errorhandler(400)
def error_handler(error):
    res = jsonify({
        'error': {
            'message': error.description['message']
        },
        'code': error.code
    })
    return res, error.code


@app.route("/")
def hello_world():
    return jsonify({"hello": "world"})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
