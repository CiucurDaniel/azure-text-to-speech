from flask import Flask

from azure_speech_service import *

app = Flask(__name__)
app.env = "development"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/tts')
def get_tts():
    result = make_tts()
    return result

@app.route('/stt')
def get_stt():
    result = make_stt()
    return result