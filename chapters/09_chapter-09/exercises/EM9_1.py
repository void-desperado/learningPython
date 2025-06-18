class Restaurant:
    def __init__(self,name,cuisine):
        self.name=name.title()
        self.cuisine=cuisine.title()

    def describe(self):
        print(f"{self.name} is the name of the restaurant and it serves {self.cuisine} cuisine")

    def open(self):
        print(f"{self.name} is now open")
