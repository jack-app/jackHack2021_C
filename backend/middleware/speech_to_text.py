from google.cloud import speech_v1p1beta1 as speech


def speech_to_text(voice_file, extension):
    client = speech.SpeechClient()

    language_code = "ja-JP"
    sample_rate_hertz = 44100

    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
    if extension == 'mp3':
        encoding = speech.RecognitionConfig.AudioEncoding.MP3

    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "enable_speaker_diarization": True,
        "audio_channel_count": 2,
    }

    voice_byte = voice_file.read()
    content = voice_byte
    audio = {"content": content}
    response = client.recognize(config=config, audio=audio)
    # words = []
    # for word in response.results[0].alternatives[0].words:
    #     words.append(word.word.split('|')[0])
    text = response.results[0].alternatives[0].transcript

    return text
