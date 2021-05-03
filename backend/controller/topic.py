from flask import jsonify, request, abort

from models.topic import Topic
from utils.check_params import check_params


def get_topics():
    topics = Topic.get_topics()

    res = []
    for topic in topics:
        topic_dict = topic.to_dict()
        res.append(topic_dict)

    return jsonify(res)


def register_topic():
    diary_requests = ['name', 'situation_type_id']

    if not check_params(request.json, diary_requests):
        abort(400, {'message': 'parameter not found'})

    name = request.json["name"]
    situation_type_id = request.json["situation_type_id"]

    if name == '':
        abort(400, {'message': 'title is null'})

    new_topic = Topic(name=name, situation_type_id=situation_type_id)
    topic_id = new_topic.post_topic()

    return jsonify({"id": topic_id})
