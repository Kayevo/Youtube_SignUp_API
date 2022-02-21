class User:

    ADMIN_TYPE = "Administrator"
    COMMON_TYPE = "Common"
    email = ""
    password = ""
    userType = ""

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password
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