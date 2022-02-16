import database

# Verify user method test
localDatabase = database.Database()

userOne = database.User("email@1.com", "pass1")

test1 = localDatabase.verifyUser(userOne)

localDatabase.addUser(userOne)

userTwo = database.User("email@2.com", "pass2")
localDatabase.addUser(userTwo)

test2 = localDatabase.verifyUser(userTwo)

print(test1)
print(test2)
