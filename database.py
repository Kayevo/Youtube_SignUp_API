import User


class Database:

    userTable = list()

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

    def findUser(self, _user):
        foundUser = False

        for currentUser in self.userTable:
            if(currentUser.email == _user.email
               and currentUser.password == _user.password):
                foundUser = True
        return foundUser

    def verifyAdminUser(self, _user):
        verifiedAdminUser = False

        for currentUser in self.userTable:
            if(currentUser.email == _user.email
               and currentUser.password == _user.password
               and currentUser.userType == User.User.ADMIN_TYPE):
                verifiedAdminUser = True
        return verifiedAdminUser
