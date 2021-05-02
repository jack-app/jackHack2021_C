from flask import jsonify,request

from models.diary import Diary


def get_diarys():
    diarys = Diary.get_diarys()

    res = []
    for diary in diarys:
        diary_dict = diary.to_dict()
        res.append(diary_dict)
    return jsonify(res)

def get_diary(diary_id):
    diary = Diary.get_diary(diary_id)

    return jsonify(diary.todict())

def register_diary():
    name = request.json["name"]
    title = request.json["title"]
    content = request.json["content"]
    user_id = request.json["user_id"]
    new_diary = Diary(name=name)
    diary_id = new_diary/post_diary()

    return jsonify({"id":diary_id}) 