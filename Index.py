import Database
import User
import Credential
from flask import Flask, request

app = Flask("YouTube")
database = Database.Database()


@app.route("/user/table", methods=["GET"])
def test():
    body = request.get_json()

    userCredentials = Credential.Credential(body["email"], body["password"])
    userTable = getUserTable(userCredentials)

    return userTable


def getUserTable(_userCredentials):
    userTable = ""

    if(database.existsUser(_userCredentials)):
        youtubeUser = database.findUser(_userCredentials)

        if(youtubeUser.verifyAdminUser()):
            userTable = database.getUserTable()

    return userTable


@app.route("/user/signup", methods=["POST"])
def userSignUp():
    body = request.get_json()

    userCredentials = Credential.Credential(body["email"], body["password"])
    user = addUserOnDabase(userCredentials, body["adminUser"])

    return user

def addUserOnDabase(_userCredentials, _isAdmin):

    user = User.User(_userCredentials.email, _userCredentials.password)

    if(_isAdmin):
        user.setAdminUser()
    else:
        user.setCommonUser()

    database.addUser(user)

    return user.getUser()


app.run(debug=True)
