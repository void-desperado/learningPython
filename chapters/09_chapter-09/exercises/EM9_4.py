class Restaurant:
    def __init__(self,name,cuisine):
        self.name=name.title()
        self.cuisine=cuisine.title()
        self.numberServed=0

    def describe(self):
        print(f"{self.name} is the name of the restaurant and it serves {self.cuisine} cuisine")

    def open(self):
        print(f"{self.name} is now open")

    def setNumberServed(self,customersServed):
        self.numberServed=customersServed

    def incrementNumberServed(self,newCustomersServed):
        self.numberServed+=newCustomersServed
