import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from db import db
from utils.error_handler import handle_bad_request, handle_not_found_request
from controller.hello import get_hello, post_hello
from controller.user import get_users, get_user, register_user

app = Flask(__name__)
CORS(app)

# error handlinghandle_bad_request
app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, handle_not_found_request)

# controller
app.add_url_rule('/hello', 'get_hello', get_hello)
app.add_url_rule('/hello', 'post_hello', post_hello, methods=['POST'])

app.add_url_rule('/users', 'get_users', get_users)
app.add_url_rule('/user/<int:user_id>', 'get_user', get_user)
app.add_url_rule('/user', 'register_user', register_user, methods={'POST'})


if __name__ == "__main__":
    load_dotenv()
    db_config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'host': os.getenv('DB_HOST'),
        'db_name': os.getenv('DB_NAME')
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(
        **db_config)
    db.init_db(app)

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
