from flask import jsonify

from models.situation_type import SituationType


def get_situation_type():
    situ_type = SituationType.get_situation_type()
    
    res = []
    for types in situ_type:
        types_dict = types.to_dict
        res.append(types_dict)
    return jsonify(res)
