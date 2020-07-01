from flask import Flask, jsonify, make_response, render_template
from flask_cors import CORS

DEBUG = True

app = Flask(__name__, #static_url_path='',
        template_folder='static')
        # static_folder='./static')
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/')
def index():
    return make_response(render_template('/index.html'))
    # return app.send_static_file('index.html')

# @app.errorhandler(404)
# def page_not_found(e):
#     return make_response(render_template('/index.html'))
#     # return app.send_static_file('index.html')

@app.route("/<path:fallback>")
def fallback(fallback):
    print('fallback = ' + fallback)
    if fallback.startswith('css/') or fallback.startswith('js/') \
        or fallback.startswith('img/') or fallback == 'favicon.ico':
            #return make_response(render_template('/' + fallback))
            return app.send_static_file(fallback)
    else:
        #return make_response(render_template('/index.html'))
        return app.send_static_file('index.html')
    #resp = make_response(render_template("/index.html"))
    #return resp

if __name__ == '__main__':
    app.run()
