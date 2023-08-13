import Dojo_pets_ninja_v2

ninja = Dojo_pets_ninja_v2.Ninja

class Pet(ninja):
    def __init__(self, name, type, tricks, fname, lname, treats, pet_food, pet) -> None:
        super().__init__(fname, lname, treats, pet_food, pet)
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        print(self.name, self.type, self.tricks, self.health, self.energy)

    def sleep(self):
        self.energy += 25
        print(self.energy)

    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.energy, self.health)

    def play(self):
        self.health += 5
        print(self.health)

    def noise(self):
        print(f"{self.type} Sound!!")


james = Pet("bob", "dog", ["chase tail", "searching"], "james", "bond", "candy", "bone", "dog")
james.feed()
james.walk()
james.bathe()