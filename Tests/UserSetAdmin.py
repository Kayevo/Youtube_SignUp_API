import sys
sys.path.append( './' )
import User

# Set admin user

userThree = User.User("email@1.com", "pass1")
userThree.setAdminUser()

print(userThree.getUser())