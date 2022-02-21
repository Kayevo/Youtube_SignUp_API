import sys
sys.path.append( './' )
import Database
import User

# Verify user method test
localDatabase = Database.Database()

userOne = User.User("email@1.com", "pass1")

test1 = localDatabase.verifyUser(userOne)

localDatabase.addUser(userOne)

userTwo = User.User("email@2.com", "pass2")
localDatabase.addUser(userTwo)

test2 = localDatabase.verifyUser(userTwo)

print(test1)
print(test2)


