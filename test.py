from functools import wraps
import pymongo
import flask

app = flask.Flask(__name__)

@app.route('/conversations')
def get_conversations():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()