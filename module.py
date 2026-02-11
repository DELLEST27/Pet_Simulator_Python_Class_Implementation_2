# This is an an incomplete 
class Pet:
    def __init__(self, name): #__Magic__
        #when creating a class object
        # Add initialize code here

        #Inside of _init_ I should set necessary properties
        self.name = name #name is variable
        self.hunger= 50
        self.energy= 50
        self.happiness= 50
    
    def status(self):
        return f"{self.name} | {self.hunger} | {self.happiness} | {self.energy}"
        
    def feed(self, food):
        self.hunger= self.hunger - food
        food= 10
        return f"{self.name} east and reduces hunger by {food}"

    def play(self, amount):
        #buddy gets happy but gets tired
        self.happiness = self.happiness + amount
        self.energy = self.energy - amount
        return f"{self.name} plays and gains {amount} happiness but loses {amount} of energy"

    def sleep(self, amount):
        self.energy= self.energy + amount
        return f"{self.name} has now gained {amount}"
    
    def check(self):
        if(self.hunger > 70 ):
            return f"{self.name} is healthy"
        elif(self.energy < 20):
            return f"{self.name} is tired"
        elif(self.happiness < 20):
            return f"{self.name} is not happy happy please please play play"