from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
sio = SocketIO(app)
app.config['SECRET_KEY'] = 'lkkkqjdlkajf2380923'
from app import routes
from app import events

