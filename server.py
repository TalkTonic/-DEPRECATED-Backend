from functools import wraps
import pymongo
import flask
from flask import request
from flask.ext.socketio import SocketIO



app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/conversations', methods=['POST'])
def get_conversations():
    #username = request.form["username"]
    #username = dataDict['username']
    #password = dataDict['password']

    #return username

    data = request.form
    print data 
    return str(data)

if __name__ == '__main__':
	socketio.run(app)
