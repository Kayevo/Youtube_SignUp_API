import Database
import User
import Credential
from flask import Flask, request

youtubeApp = Flask("YouTube")
database = Database.Database()


@youtubeApp.route("/user/table", methods=["GET"])
def userTable():
    bodyJson = request.get_json()
    bodyData = request.get_data()

    if(bodyJson):
        userCredentials = Credential.Credential(
            bodyJson["email"], bodyJson["password"])
    elif(bodyData):
        userCredentials = Credential.Credential(
            bodyData["email"], bodyData["password"])

    if(userCredentials):
        userTable = getUserTable(userCredentials)

    return userTable


def getUserTable(_userCredentials):
    userTable = ""

    if(database.existsUser(_userCredentials)):
        youtubeUser = database.findUser(_userCredentials)

        if(youtubeUser.verifyAdminUser()):
            userTable = database.getUserTable()

    return userTable


@youtubeApp.route("/user/signup", methods=["POST"])
def userSignUp():
    bodyJson = request.get_json()
    bodyData = request.get_data()
    isAdminUser = False

    if(bodyJson):
        userCredentials = Credential.Credential(
            bodyJson["email"], bodyJson["password"])
        isAdminUser = bodyJson["isAdminUser"]
    elif(bodyData):
        userCredentials = Credential.Credential(
            bodyData["email"], bodyData["password"])
        isAdminUser = bodyData["isAdminUser"]

    user = addUserOnDabase(userCredentials, isAdminUser)

    return user


def addUserOnDabase(_userCredentials, _isAdmin):

    user = User.User(_userCredentials.email, _userCredentials.password)

    if(_isAdmin):
        user.setAdminUser()
    else:
        user.setCommonUser()

    database.addUser(user)

    return user.getUser()


youtubeApp.run(debug = True)
