from app import app
from flask import render_template
from app import sio

@app.route("/", methods=['GET', 'POST'])
def chat():
    return render_template("client.html")


