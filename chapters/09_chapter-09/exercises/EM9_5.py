class User:
    def __init__(self,firstName,lastName):
        self.firstName=firstName.title()
        self.lastName=lastName.title()
        self.loginAttempts=0

    def describe(self):
        print(f"The user's full name is {self.firstName} {self.lastName}")

    def greet(self):
        print(f"Hello, {self.firstName} {self.lastName}")
        
    def resetLoginAttempts(self):
        self.loginAttempts=0

    def incrementLoginAttempts(self):
        self.loginAttempts+=1