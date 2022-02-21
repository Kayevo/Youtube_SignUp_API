import Database
import User
from flask import Flask, request

app = Flask("YouTube")
youtubeDatabase = Database.Database()


@app.route("/user/table", methods=["GET"])
def test():
    body = request.get_json()

    userTable = ""
    _user = User.User(body["email"], body["password"])

    # verified = youtubeDatabase.findUser(_user)
    # userIsAdmin = youtubeDatabase.verifyAdminUser(_user)

    existsUser = youtubeDatabase.existsUser(_user)
    currentUser = youtubeDatabase.findUser(_user)

    # if(youtubeDatabase.findUser(_user)
    #    and youtubeDatabase.verifyAdminUser(_user)):
    #     userTable = youtubeDatabase.getUserTable()

    if(youtubeDatabase.existsUser(_user)):
        youtubeUser = youtubeDatabase.findUser(_user)

        if(youtubeUser.verifyAdminUser()):
            userTable = youtubeDatabase.getUserTable()

    return userTable


@app.route("/user/signup", methods=["POST"])
def userSignUp():
    body = request.get_json()

    youtubeUser = User.User(body["email"], body["password"])

    if(body["adminUser"] == True):
        youtubeUser.setAdminUser()
    else:
        youtubeUser.setCommonUser()

    youtubeDatabase.addUser(youtubeUser)

    return youtubeUser.getUser()


app.run(debug=False)
