from flask import Flask
from flask_socketio import SocketIO, emit, send
from flask.templating import render_template
app = Flask(__name__)
io = SocketIO(app)

messages = []

@app.route("/")
def index():
    return render_template("chat.html")

@io.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg)
    emit('getMessage', msg, json=True, broadcast=True)

@io.on('message')
def message_handle(msg):
    send(messages)
    
if __name__ == "__main__":
    io.run(app, debug=True)