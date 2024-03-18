from flask import Flask, render_template 
from flask_socketio import SocketIO, send

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()
    .