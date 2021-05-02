from google.cloud import speech


def speech_to_text(voice_file):
    client = speech.SpeechClient()

    language_code = "ja-JP"
    sample_rate_hertz = 44100
    encoding = speech.RecognitionConfig.AudioEncoding.MP3
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "enable_speaker_diarization": True,
        # "diarization_speaker_count": people_num
    }

    content = voice_file.read()
    audio = {"content": content}
    response = client.recognize(config, audio)

    return response
