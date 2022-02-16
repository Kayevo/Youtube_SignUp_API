from typing import List

from click import password_option


class User:

    email = ""
    password = ""

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password

    def getUser(self):
        stringUser = ""

        stringUser += "E-mail: " + self.email + "\n"
        stringUser += "Password: " + self.password + "\n\n"
        return stringUser


class Database:

    userTable = list()
    adminUserTable = list()

    def __init__(self):
        self.userTable = list()
        self.adminUserTable = list()

    def addUser(self, _user):
        self.userTable.append(_user)

    def getUserTable(self):
        stringUserTable = ""
        for currentUser in self.userTable:
            stringUserTable += currentUser.getUser()
        return stringUserTable

    def verifyUser(self, _user):
        verifiedUser = False

        for currentUser in self.userTable:
            if(currentUser.email == _user.email
               and currentUser.password == _user.password):
                verifiedUser = True
        return verifiedUser





