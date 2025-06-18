class User:
    def __init__(self,firstName,lastName):
        self.firstName=firstName.title()
        self.lastName=lastName.title()

    def describe(self):
        print(f"The user's full name is {self.firstName} {self.lastName}")

    def greet(self):
        print(f"Hello, {self.firstName} {self.lastName}")