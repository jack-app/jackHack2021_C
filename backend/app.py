import os

from flask import Flask
from flask_cors import CORS

from utils.error_handler import handle_bad_request, handle_not_found_request
from controller.hello import hello

app = Flask(__name__)
CORS(app)

# error handlinghandle_bad_request
app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, handle_not_found_request)

# controller
app.add_url_rule('/hello', 'hello', hello)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
