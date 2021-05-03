from flask import jsonify, request, abort

from models.diary import Diary
from utils.check_params import check_params


def get_diarys():
    diarys = Diary.get_diarys()

    res = []
    for diary in diarys:
        diary_dict = diary.to_dict()
        res.append(diary_dict)
    return jsonify(res)


def get_diary(diary_id):
    diary = Diary.get_diary(diary_id)

    return jsonify(diary.to_dict())


def register_diary():
    diary_requests = ['title', 'content', 'user_id']

    if not check_params(request.json, diary_requests):
        abort(400, {'message': 'parameter not found'})

    title = request.json["title"]
    content = request.json["content"]
    user_id = request.json["user_id"]

    if title == '':
        abort(400, {'message': 'title is null'})
    if content == '':
        abort(400, {'message': 'content is null'})

    new_diary = Diary(title=title, content=content,
                      user_id=user_id)
    diary_id = new_diary.post_diary()

    return jsonify({"id": diary_id})
