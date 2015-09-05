from functools import wraps
import pymongo
import flask

app = flask.Flask(__name__)

@app.route('/conversations/<username>/<password>')
def get_conversations(username,password):
    return username + "pass" +  password

if __name__ == '__main__':
    app.run()