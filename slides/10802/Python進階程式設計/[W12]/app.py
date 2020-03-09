from flask import Flask, render_template
from flask_socketio import SocketIO
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '1126'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    user = {'first':'Jiawei', 'last': 'Chang'}
    return render_template('view.html', date ='2019/11/26', name = user)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

def savelog(name, message):
    conn = sqlite3.connect('log.db')
    cursor = conn.cursor()
    insert_query = 'INSERT INTO logs VALUES(?, ?, ?)'
    cursor.execute(insert_query, (None, name, message))
    conn.commit()
    conn.close()

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    if 'user_name' in json.keys():
        savelog(json['user_name'], json['message'])

if __name__ == '__main__':
    socketio.run(app, debug=True)
