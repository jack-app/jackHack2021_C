from flask import jsonify, request, abort

from models.situation_type import SituationType
from utils.check_params import check_params


def get_situation_type():
    situation_type = SituationType.get_situation_type()

    res = []
    for types in situation_type:
        types_dict = types.to_dict()
        res.append(types_dict)

    return jsonify(res)


def resister_situation_type():
    diary_requests = ['name']

    if not check_params(request.json, diary_requests):
        abort(400, {'message': 'parameter not found'})

    name = request.json["name"]

    if name == '':
        abort(400, {'message': 'title is null'})

    new_situation_type = SituationType(name=name)
    situation_type_id = new_situation_type.post_situation_type()

    return jsonify({"id": situation_type_id})
