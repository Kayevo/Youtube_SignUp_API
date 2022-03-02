import User
import json


class Database:

    userTable = list()

    def addUser(self, _user):
        user = _user.parseToJson()
        self.userTable.append(user)
        return user

    def getUserTable(self):
        return self.userTable

    def findUser(self, _userCredentials):
        foundUser = User.User("", "")

        for currentUser in self.userTable:
            if(currentUser["email"] == _userCredentials.email
               and currentUser["password"] == _userCredentials.password):
                foundUser.email = currentUser["email"]
                foundUser.password = currentUser["password"]
                foundUser.userType = currentUser["userType"]
        return foundUser

    def existsUser(self, _userCredentials):
        existsUser = False

        for currentUser in self.userTable:
            if(currentUser["email"] == _userCredentials.email
                and currentUser["password"] == _userCredentials.password):
                existsUser = True
        return existsUser
