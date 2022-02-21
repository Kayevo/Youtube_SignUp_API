from Credential import Credential


class User(Credential):

    def __init__(self, _email, _password):

        super().__init__(_email, _password)
        self.ADMIN_TYPE = "Administrator"
        self.COMMON_TYPE = "Common"
        self.userType = self.COMMON_TYPE

    def getUser(self):
        stringUser = ""

        stringUser += "E-mail: " + self.email + "\n"
        stringUser += "Password: " + self.password + "\n"
        stringUser += "Type: " + self.userType + "\n\n"
        return stringUser

    def setAdminUser(self):
        self.userType = self.ADMIN_TYPE

    def setCommonUser(self):
        self.userType = self.COMMON_TYPE

    def verifyAdminUser(self):
        isAdminUser = False
        if(self.userType == self.ADMIN_TYPE):
            isAdminUser = True
        return isAdminUser