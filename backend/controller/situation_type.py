from flask import jsonify, request

from models.situation_type import SituationType


def get_situation_type():
    situation_type = SituationType.get_situation_type()

    res = []
    for types in situation_type:
        types_dict = types.to_dict()
        res.append(types_dict)

    return jsonify(res)


def resister_situation_type():
    name = request.json["name"]
    new_situation_type = SituationType(name=name)
    situation_type_id = new_situation_type.post_situation_type()

    return jsonify({"id": situation_type_id})
