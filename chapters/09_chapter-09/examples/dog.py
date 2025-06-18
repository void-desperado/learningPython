class Dog:
    def __init__(self,name,age):
        self.name=name.title()
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting!")

    def rollOver(self):
        print(f"{self.name} has rolled over")

myDog=Dog("whiskey",4)

print(myDog.name)
print(myDog.age)

myDog.sit()
myDog.rollOver()