
from flask import Flask, request, jsonify
import speech_recognition as sr
import tempfile

app = Flask(__name__)
recognizer = sr.Recognizer()

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files["file"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        file.save(temp_audio.name)
        with sr.AudioFile(temp_audio.name) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language="ar-SA")
    return jsonify({"text": text})

if name == "__main__":
    app.run(host="0.0.0.0", port=5000)