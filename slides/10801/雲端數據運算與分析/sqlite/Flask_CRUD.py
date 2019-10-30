import flask
from flask_cors import *
from flask import request
from flask import jsonify
import sqlite3


def add_user(name, email, password):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    insert_query = 'INSERT INTO users VALUES(?, ?, ?, ?)'
    cursor.execute(insert_query, (None, name, email, password))
    conn.commit()
    conn.close()
    return "Add the user successfully!"

def update_user(uid, name, email, password):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    update_query = 'UPDATE users SET name=?, email=?, password=? WHERE id=?'
    cursor.execute(update_query, (name, email, password, uid))
    conn.commit()
    conn.close()
    return "Update the user successfully!"


def delete_user(id):
    if request.method == 'POST' or request.method == 'GET': 
        id = request.values['id']
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        delete_query = 'DELETE FROM users WHERE id=?'
        cursor.execute(delete_query, (id,))
        conn.commit()
        conn.close()
        return "Remove the user successfully!"


def get_user(name):
    user = {}
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    query_one_query = 'SELECT * FROM users WHERE name=?'
    result = cursor.execute(query_one_query, (name,)).fetchone()
    if result is None:
        return "None"
    user.update({result[0]:{'name': result[1], 'email': result[2], 'pwd': result[3]}})
    conn.close()
    return user


def get_all_user():
    users = {}
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    query_one_query = 'SELECT * FROM users'
    for item in cursor.execute(query_one_query):
        user = {'name': item[1], 'email': item[2], 'pwd': item[3]};
        users.update({item[0]:user})
    conn.close()
    return users


app = flask.Flask(__name__)
CORS(app, resources=r'/*')
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Hello Flask!</h1>"


@app.route('/users/all', methods=['GET', 'POST'])
def getAllUsers():
    return get_all_user()

@app.route('/user', methods=['GET', 'POST'])
def getUser():
    if request.method == 'POST' or request.method == 'GET': 
        name = request.values['name'] 
        return get_user(name)
    else:
        return "Error: No name provided. Please specify a name."

@app.route('/remove', methods=['GET', 'POST'])
def removeUser():
    if request.method == 'POST' or request.method == 'GET': 
        id = request.values['id'] 
        return delete_user(id)
    else:
        return "Error: No ID provided. Please specify an ID."

@app.route('/add', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST' or request.method == 'GET': 
        name = request.values['name']
        email = request.values['email']
        password = request.values['password']
        return add_user(name, email, password)
    else:
        return "Error: No Data provided. Please specify a User Data."

@app.route('/update', methods=['GET', 'POST'])
def updateUser():
    if request.method == 'POST' or request.method == 'GET': 
        uid = request.values['uid']
        name = request.values['name']
        email = request.values['email']
        password = request.values['password']
        return update_user(int(uid), name, email, password)
    else:
        return "Error: No Data provided. Please specify a User Data."


app.run()
