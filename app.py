from flask import Flask,render_template,request
import os
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/send',methods=['GET'])
def send():
    room=request.args.get('room')
    name=request.args.get('name')
    msg=request.args.get('msg')
    data=""
    if os.path.isfile(room+'.txt'):
        with open(room+'.txt',mode='r') as f:
            data=f.read()
    data+=name+': '+msg+'<br/>'
    with open(room+'.txt',mode='w') as f:
        f.write(data)
    return data

@app.route('/update',methods=['GET'])
def update():
    room=request.args.get('room')
    data=""
    if os.path.isfile(room+'.txt'):
        with open(room+'.txt',mode='r') as f:
            data=f.read()
    return data

if __name__=="__main__": #直接執行
    app.run()