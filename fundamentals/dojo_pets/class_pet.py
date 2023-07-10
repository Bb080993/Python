
class Pet:
    def __init__(self, name , type , tricks, health, energy ):
        self.name= name
        self.pet_type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    def sleep(self):
        self.energy+=25
        print(f"Energy is {self.energy}")
        return self
    def eat(self):
        self.energy+=5
        self.health+=10
        print(f"Energy is {self.energy}, health is {self.health}")
        return self
    def play(self):
        self.health+=5
        print(f"Health is {self.health}")
        return self
    def noise(self):
        if self.pet_type=="cat":
            print("Meow")
            return self
        elif self.pet_type=="dog":
            print("Woof")
            return self
        elif self.pet_type=="mouse":
            print("Squeak")
            return self
