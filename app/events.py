from app import sio
from flask import request
import pdb


# update all the clients screens
@sio.on('message')
def handle_message(msg):
    # send to all clients
    print("connected")
    sio.emit('message', msg)




    

