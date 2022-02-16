import database
from flask import Flask, request

app = Flask("YouTube")
youtubeDatabase = database.Database()


@app.route("/users/database", methods=["GET"])
def test():
    body = request.get_json()
    return youtubeDatabase.getUserTable()


@app.route("/signup/user", methods=["POST"])
def userSignUp():
    body = request.get_json()

    youtubeUser = database.User(body["email"], body["password"])
    youtubeDatabase.addUser(youtubeUser)

    #(body["email"], body["password"], localDatabase)

    return youtubeUser.getUser()


@app.route("/signup/adminuser", methods=["POST"])
def adminUserSignUp():
    body = request.get_json()

    youtubeUser = database.User(body["email"], body["password"])
    youtubeDatabase.addUser(youtubeUser)

    #(body["email"], body["password"], localDatabase)

    return youtubeUser.getUser()


app.run()
