from class_pet import Pet
class Ninja():
    def __init__(self, first_name , last_name , treats , pet_food , pet_type):
        self.first_name= first_name
        self.last_name= last_name
        self.treats= treats
        self.pet_food=pet_food
        self.pet_type=pet_type
        self.pet=None
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

ninja_Brittany=Ninja("Brittany", "Francis", "cat treats", "iams", "cat")
print(ninja_Brittany.pet_food)

pet_Cobu_Cat=Pet("Cobu", "cat", "headboop", 50, 25)
print(pet_Cobu_Cat.energy)
ninja_Brittany.pet=pet_Cobu_Cat
print(ninja_Brittany.pet.name)
print(pet_Cobu_Cat.health)
ninja_Brittany.walk().feed().walk()
pet_Cobu_Cat.noise().sleep()
ninja_Brittany.bathe()
print(pet_Cobu_Cat.health)

