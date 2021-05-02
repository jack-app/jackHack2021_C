from flask import jsonify

from models.topic import Topic


def get_topics():
    topics = Topic.get_topics()

    res = []
    for topic in topics:
        topic_dict = topic.to_dict
        res.append(topic_dict)
    return jsonify(res)
    