from flask import jsonify, request

from models.topic import Topic


def get_topics():
    topics = Topic.get_topics()

    res = []
    for topic in topics:
        topic_dict = topic.to_dict()
        res.append(topic_dict)

    return jsonify(res)


def register_topic():
    name = request.json["name"]
    situation_type_id = request.json["situation_type_id"]
    new_topic = Topic(name=name, situation_type_id=situation_type_id)
    topic_id = new_topic.post_topic()

    return jsonify({"id": topic_id})
