from flask import jsonify

from models.question import Question


def get_questions(topic_id):
    questions = Question.get_questions(topic_id)

    res=[]
    for question in questions:
        question_dict = question.to_dict
        res.append(question_dict)
    return jsonify(res)   