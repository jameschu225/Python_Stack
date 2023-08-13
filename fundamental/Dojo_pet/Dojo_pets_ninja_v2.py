class Ninja:
    
    def __init__(self, fname , lname , treats , pet_food , pet) -> None:
        self.first_name = fname
        self.last_name = lname
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        print(self.first_name, self.last_name, self.pet, self.treats, self.pet_food)

    def walk(self):
        Pet.play(self.pet)

    def feed(self):
        Pet.eat(self.pet)

    def bathe(self):
        Pet.noise(self.pet)