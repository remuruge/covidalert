from __future__ import print_function
from flask import Flask, jsonify, request, current_app
import requests
import logging
import time
import os
from datetime import datetime

app = Flask(__name__)
data = []
names = []
#os.environ['NO_PROXY'] = '127.0.0.1'
userList = []

@app.route('/', methods=['GET'])
def root():
    time.sleep(1)
    return "Hello! I'm covid alerting system."

@app.route('/covid/user/<email>', methods=['GET'])
def user_valid(email):
    data = create_data()
    if not any(d['email'] == email for d in data):
        return jsonify({'Invalid user': email}), 200
    date = [d['date'] for d in data if d['email'] == email]
    names = [d['name'] for d in data if d['date'] == date]
    return jsonify({'Valid user': names}), 200

@app.route('/alert', methods=['GET'])
def user_search():
    email_id = request.args.get('email')
    print(email_id)
    users = get_users()
    userList = users['userList']
    get_visits()
    maybeInfected = get_aymptomatic(userList, email_id)
    if not maybeInfected:
        return jsonify(message="User not visited the branch recently"), 400
    else:
        return jsonify(maybeInfected), 200

def get_users():
    # users = request.form.get('userList')
    # users = request.get_json()
    r = requests.get('http://localhost:8080/users')
    return r.json()

def get_visits():
    r = requests.get('http://localhost:3000/visits?date=2020-07-28')
    return r.json()

def get_aymptomatic(userList, email):
    flag = 0

    for user in userList:
        if user['email'] == email:
            flag = 1
            keyUserVisit = [(visit['branchId'],visit['date'],visit['userId']) for visit in get_visits() if visit['userId'] == user['userId']]
            #print(keyUserVisit)
            for (visitBranch, visitDt, keyUserId) in keyUserVisit:
                usersIdentified = [visits for visits in get_visits() if (visits['branchId'] == visitBranch and datetime.strptime(visits['date'],"%Y-%m-%dT%H:%M:%S.%fZ") == datetime.strptime(visitDt,"%Y-%m-%dT%H:%M:%S.%fZ"))]
                aymptUsers=filter_keyUser(usersIdentified,keyUserId)
                #print(get_user(userList, aymptUsers))
                return get_user(userList, aymptUsers)
    if flag == 0:
            print('Invalid user ' + email)
            return []

def get_user(userList, users):
    asymptomatic_users=[]
    for u in users:
        for user in userList:
            if user['userId'] == u['userId']:
                u['name']=user['name']
                u['email']=user['email']
                u['address']=user['address']
                u['phone']=user['phone']
        asymptomatic_users.append(u)
    return asymptomatic_users

def filter_keyUser(usersIdentified,keyUserId):
    maybeInfected = [user for user in usersIdentified if user['userId'] != keyUserId]
    return maybeInfected


def create_data():
    data = [
        {"id": 1, "name":"Stephen Brennan","email": "StephenBrenann@gmail.com","Add":"5 St. Powers Walk Cresent","Ph":"0851180846", "acct":"0000001", "branchId":"1", "date":"2020-07-28"},
        {"id": 2, "name":"Alex Smith", "email": "AlexSmith@gmail.com", "Add":"5 St. Powers Walk Cresent", "Ph":"0851183546", "acct":"0000002", "branchId":"2", "date":"2020-07-27"},
        {"id": 3, "name":"David Jones", "email": "DavidJones@gmail.com", "Add":"5 St. Powers Walk Cresent", "Ph":"0851183546", "acct":"0000003", "branchId":"3", "date":"2020-07-28"},
        {"id": 4, "name":"Wellington Waters V", "email": "damian.lockman@gmail.com", "Add":"5135 Bartoletti Lodge Suite 372 Ebertburgh, WI 78211", "Ph":"0851183546", "acct":"0000004", "branchId":"4", "date":"2020-07-28"},
        {"id": 5, "name":"Antone Kautzer III", "email": "mayert.hollie@gmail.com", "Add":"5 St. Powers Walk Cresent", "Ph":"0851183546", "acct":"0000005", "branchId":"5", "date":"2020-07-27"}
    ]
    return data


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    data = create_data()
    app.run(debug=True)