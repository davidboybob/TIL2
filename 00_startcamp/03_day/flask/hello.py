
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'I want quit qy'


@app.route('/ssafy')
def ssafy():
    return 'This is ssafy'

