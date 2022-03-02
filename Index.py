from email import message
from urllib import response
import Database
import User
import Credential
import json
from flask import Flask, make_response, request

youtubeApp = Flask("YouTube")
database = Database.Database()


@youtubeApp.route("/user/table", methods=["POST"])
def userTable():
    bodyJson = request.get_json()
    bodyData = json.loads(request.get_data())
    message = ""
    status = 500
    response = make_response(message, status)

    if(bodyJson):
        userCredentials = Credential.Credential(
            bodyJson["email"], bodyJson["password"])
    elif(bodyData):
        userCredentials = Credential.Credential(
            bodyData["email"], bodyData["password"])

    if(userCredentials):
        response = getUserTable(userCredentials)

    return response


def getUserTable(_userCredentials):
    message = ""
    status = 500
    response = make_response(message, status)

    if(database.existsUser(_userCredentials)):
        youtubeUser = database.findUser(_userCredentials)

        if(youtubeUser.verifyAdminUser()):
            message = json.dumps(database.getUserTable())
            status = 200
        else:
            message = "User dont have access"
            status = 401
    else:
        message = "User not exist"
        status = 401

    response = make_response(message, status)

    return response


@youtubeApp.route("/user/signup", methods=["POST"])
def userSignUp():
    bodyJson = request.get_json()
    bodyData = json.loads(request.get_data())
    isAdminUser = False
    message = ""
    status = 500

    if(bodyJson):
        userCredentials = Credential.Credential(
            bodyJson["email"], bodyJson["password"])
        isAdminUser = bodyJson["isAdminUser"]
    elif(bodyData):
        userCredentials = Credential.Credential(
            bodyData["email"], bodyData["password"])
        isAdminUser = bodyData["isAdminUser"]

    if(database.existsUser(userCredentials)):
        message = "User already exist."
        status = 406
    else:
        user = addUserOnDabase(userCredentials, isAdminUser)
        message = user
        status = 200

    response = make_response(message, status)
    return response


def addUserOnDabase(_userCredentials, _isAdmin):

    user = User.User(_userCredentials.email, _userCredentials.password)
    userJson = {}

    if(_isAdmin):
        user.setAdminUser()
    else:
        user.setCommonUser()

    userJson = database.addUser(user)

    return userJson


youtubeApp.run(debug=True)
