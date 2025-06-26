from flask import Flask, request, send_file
from TTS.api import TTS
import uuid

app = Flask(__name__)
tts = TTS("tts_models/en/ljspeech/glow-tts", progress_bar=False, gpu=False)

@app.route('/tts', methods=['POST'])
def synthesize():
    data = request.get_json()
    text = data.get("text", "Hello world")
    filename = f"/tmp/{uuid.uuid4()}.wav"
    tts.tts_to_file(text=text, file_path=filename)
    return send_file(filename, mimetype="audio/wav")
