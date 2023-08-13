import Dojo_pets_pets_v1

Pets = Dojo_pets_pets_v1.Pet

class Ninja:
    
    def __init__(self, fname , lname , treats , pet_food , pet) -> None:
        self.first_name = fname
        self.last_name = lname
        self.pet = Pets( name=" bob", type = pet, tricks= ["chase tail", "searching"])
        self.treats = treats
        self.pet_food = pet_food
        print(self.first_name, self.last_name, self.pet, self.treats, self.pet_food)

    def walk(self):
        Pets.play(self.pet)

    def feed(self):
        Pets.eat(self.pet)

    def bathe(self):
        Pets.noise(self.pet)

james = Ninja("james", "bond", "candy", "bone", "dog")
james.feed()
james.walk()
james.bathe()