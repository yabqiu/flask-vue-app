from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
