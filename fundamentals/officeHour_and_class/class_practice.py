"""- Simple game character class: Character
            - attributes
                - name
                - energy
                - weapons

            - methods
                - eat(food_name)
                    - print "Fred ate pizza"
                    - increase energy by 5
                    - return energy level

                - walk
                    - decrease energy by 1
                    - return energy level

                - add_weapon(weapon_name)
                    - add to weapons
                    - return list of weapons
"""

class Character:
    def __init__(self, name, energy, weapons):
        self.name=name
        self.energy= energy
        self.weapons=weapons
    
    def eat(self, food_name):
        print(f"Fred ate {food_name}")
        self.energy+=5
        return self.energy
    
    def walk(self):
        self.energy-=1
        return self.energy
    
    def add_weapon(self, weapon_name):
        self.weapons.append(weapon_name)
        return self.weapons
    
soldier=Character("Brittany", 100, ["sword", "knife"])
print(soldier.weapons)
print(soldier.eat("pasta"))
print(soldier.walk())
soldier.add_weapon("gun")
print(soldier.weapons)