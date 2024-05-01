import time

class VirtualPet:
    def __init__(self, name, species, owner_phone_number):
        self.name = name
        self.species = species
        self.hunger = 0
        self.happiness = 100
        self.owner_phone_number = owner_phone_number
        self.last_update_time = time.time()

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

    def update(self):
        current_time = time.time()
        time_passed = current_time - self.last_update_time
        if time_passed >= 7200:  # 2 hours
            self.hunger += 10
            self.happiness -= 15
            self.last_update_time = current_time
            if self.hunger <= 20 or self.happiness <= 20:
                self.send_notification()

    def send_notification(self):
        # Placeholder for sending SMS notification
        print(f"Sending SMS to {self.owner_phone_number}: Your pet {self.name} needs attention! Hunger: {self.hunger}, Happiness: {self.happiness}")

    def is_alive(self):
        return self.hunger > 0 and self.happiness > 0
