from Credential import Credential
import json


class User(Credential):

    userType = ""

    def __init__(self, _email, _password):

        super().__init__(_email, _password)
        self.ADMIN_TYPE = "Administrator"
        self.COMMON_TYPE = "Common"
        self.userType = self.COMMON_TYPE

    def parseToJson(self):
        userJson = json.loads(json.dumps(self.__dict__))
        return userJson

    def setAdminUser(self):
        self.userType = self.ADMIN_TYPE

    def setCommonUser(self):
        self.userType = self.COMMON_TYPE

    def verifyAdminUser(self):
        isAdminUser = False
        if(self.userType == self.ADMIN_TYPE):
            isAdminUser = True
        return isAdminUser
