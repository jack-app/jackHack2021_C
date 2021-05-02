from flask import jsonify, request, abort

from utils.check_file import allwed_file
from middleware.speech_to_text import speech_to_text
from middleware.text_embedding import text_embedding


def extract_words():
    if 'files' not in request.files:
        abort(400, {'message': 'parameter [file] is not found'})
    voice_file = request.files['files']

    if voice_file.filename == '':
        abort(400, {'message': 'file is not found'})

    if voice_file and allwed_file(voice_file.filename):
        text = speech_to_text(voice_file)
        vec = text_embedding(text)

        return jsonify({"vector": vec.tolist()})
    elif allwed_file(voice_file.filename):
        abort(400, {'message': 'extension is invalid'})
    else:
        abort(400, {'message': 'unknown error'})
