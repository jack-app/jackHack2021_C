from flask import jsonify, request, abort

from utils.check_file import allwed_file
from middleware.speech_to_text import speech_to_text


def extract_words():
    if 'files' not in request.files:
        abort(400, {'message': 'parameter [file] is not found'})
    voice_file = request.files['files']

    if voice_file.filename == '':
        abort(400, {'message': 'file is not found'})

    if voice_file and allwed_file(voice_file.filename):
        res = speech_to_text(voice_file)
        print(res)

        # return jsonify(res)
        return jsonify({"success": "congratulation"})
    elif allwed_file(voice_file.filename):
        abort(400, {'message': 'extension is invalid'})
    else:
        abort(400, {'message': 'unknown error'})
