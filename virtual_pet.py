# virtual_pet.py

class VirtualPet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 0
        self.happiness = 100

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100

    def status(self):
        return {
            "name": self.name,
            "species": self.species,
            "hunger": self.hunger,
            "happiness": self.happiness
        }
