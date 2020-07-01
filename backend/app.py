from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
def index():
    return app.send_static_file('/index.html')


@app.route("/<path:fallback>")
def fallback(fallback):
    if fallback.startswith('css/') or fallback.startswith('js/')\
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
