from flask import Flask, render_template, request

app = Flask(__name__)

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

def choose_animal():
    print("Welcome to the Virtual Pet Adoption Center!")
    print("What kind of animal would you like to adopt?")
    print("1. Cat")
    print("2. Dog")
    print("3. Bunny")
    print("4. Bird")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adopt', methods=['POST'])
def adopt_pet():
    choice = request.form['animal_choice']
    species_map = {
        '1': "Cat",
        '2': "Dog",
        '3': "Bunny",
        '4': "Bird"
    }
    species = species_map[choice]
    name = request.form['pet_name']
    pet = VirtualPet(name, species)
    pet_info = pet.status()
    return render_template('pet_info.html', pet_info=pet_info)

if __name__ == '__main__':
    app.run(debug=True)
