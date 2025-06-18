class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.distance=0

    def describe(self):
        return f"{self.make} {self.model} {self.year}"
    
    def readDistance(self):
        print(f"This car has {self.distance} miles on it")

    def updateDistance(self, mileage):
        if mileage >= self.distance:
            self.distance = mileage
        else:
             print("You can't roll back an distance!")

    def incrementDistance(self, miles):
        self.distance += miles
    
myCar=Car('audi','R8',2016)
print(f"{myCar.describe()}")
myCar.updateDistance(20)
myCar.readDistance()
myCar.incrementDistance(10)
myCar.readDistance()