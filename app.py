from flask import Flask,render_template
from flask_socketio import SocketIO,send

import socketio
app=Flask(__name__)
socketio=SocketIO(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@socketio.on('message')
def onmessage(data):
    send(data,broadcast=True) 

if __name__=="__main__": #直接執行
    app.run()