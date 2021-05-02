import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from db import db
from utils.error_handler import handle_bad_request, handle_not_found_request
from controller.hello import get_hello, post_hello
from controller.user import get_users, get_user, register_user
from controller.diary import get_diarys, get_diary, register_diary
from controller.situation_type import get_situation_type, resister_situation_type
from controller.topic import get_topics, register_topic
from controller.extract_words import extract_words

app = Flask(__name__)
CORS(app)

# error handlinghandle_bad_request
app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, handle_not_found_request)

# controller
# sample
app.add_url_rule('/hello', 'get_hello', get_hello)
app.add_url_rule('/hello', 'post_hello', post_hello, methods=['POST'])

# users
app.add_url_rule('/users', 'get_users', get_users)
app.add_url_rule('/user/<int:user_id>', 'get_user', get_user)
app.add_url_rule('/user', 'register_user', register_user, methods={'POST'})

# diary
app.add_url_rule('/diary', 'get_diaries', get_diarys)
app.add_url_rule('/diary/<int:diary_id>', 'get_diary', get_diary)
app.add_url_rule('/diary', 'register_diary', register_diary, methods={'POST'})

# situation_type
app.add_url_rule('/situation_type', 'get_situation_type', get_situation_type)
app.add_url_rule('/situation_type', 'resister_situation_type',
                 resister_situation_type, methods={'POST'})

# topic
app.add_url_rule('/topic', 'get_topic', get_topics)
app.add_url_rule('/topic', 'register_topic',
                 register_topic, methods={'POST'})

# word processing
app.add_url_rule('/extract-word', 'extract-word',
                 extract_words, methods={'POST'})


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
