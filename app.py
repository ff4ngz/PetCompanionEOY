from flask import Flask, render_template, request, redirect, url_for, session
import smtplib
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

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
    
    session['phone_number'] = phone_number
    send_sms(phone_number, f"Congratulations! You've adopted a {species} named {name}!")
    
    return redirect(url_for('home'))

def send_sms(phone_number, message):
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    
    email_message = f"From: {sender_email}\nTo: {phone_number}@sms_gateway.com\nSubject: Virtual Pet Adoption\n\n{message}"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, f"{phone_number}@sms_gateway.com", email_message)
    server.quit()

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
