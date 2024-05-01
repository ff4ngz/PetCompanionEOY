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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adopt', methods=['POST', 'GET'])
def adopt_pet():
    if request.method == 'POST':
        choice = request.form['animal_choice']
        species_map = {
            '1': "Cat",
            '2': "Dog",
            '3': "Bunny",
            '4': "Bird"
        }

        species = species_map[choice]
        return render_template('name_pet.html', species=species, animal_choice=choice) # Pass species and animal_choice
    else:
        # This block handles the GET request
        animal_choice = request.args.get('animal_choice')
        species_map = {
            '1': "Cat",
            '2': "Dog",
            '3': "Bunny",
            '4': "Bird"
        }

        species = species_map[animal_choice]
        pet_name_prompt = f"What would you like to name your {species.lower()}?"
        return render_template('name_pet.html', pet_name_prompt=pet_name_prompt, animal_choice=animal_choice, species=species) # Pass species and animal_choice

        
@app.route('/confirm', methods=['POST'])
def confirm_pet():
    name = request.form['pet_name']
    species = request.form['species']
    phone_number = request.form['phone_number']
    
    # Store the user's phone number for future use
    # You can store it in a session, database, or any other suitable storage mechanism
    session['phone_number'] = phone_number

@app.route('/feed', methods=['POST'])
def feed_pet():
    name = request.form['pet_name']
    species = request.form['species']
    pet = VirtualPet(name, species)
    pet.feed()
    pet_info = pet.status()
    phone_number = request.form['phone_number']
    return render_template('pet_info.html', pet_info=pet_info, phone_number=phone_number)

@app.route('/play', methods=['POST'])
def play_with_pet():
    name = request.form['pet_name']
    species = request.form['species']
    pet = VirtualPet(name, species)
    pet.play()
    pet_info = pet.status()
    phone_number = request.form['phone_number']
    return render_template('pet_info.html', pet_info=pet_info, phone_number=phone_number)

if __name__ == '__main__':
    app.run(debug=False)
