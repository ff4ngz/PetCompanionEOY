from flask import Flask, render_template, request, redirect
from virtual_pet import VirtualPet

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/adopt', methods=['GET', 'POST'])
def adopt_pet():
    if request.method == 'POST':
        animal_choice = int(request.form['animal_choice'])
        pet_name_prompt = f"What would you like to name your {'cat' if animal_choice == 1 else 'dog' if animal_choice == 2 else 'bunny' if animal_choice == 3 else 'bird'}?"
        return render_template('name_pet.html', pet_name_prompt=pet_name_prompt)
    else:
        return render_template('index.html')

# Define routes for adopting specific animals
@app.route('/adopt/cat', methods=['GET'])
def adopt_cat():
    return redirect('/adopt')

@app.route('/adopt/dog', methods=['GET'])
def adopt_dog():
    return redirect('/adopt')

@app.route('/adopt/bunny', methods=['GET'])
def adopt_bunny():
    return redirect('/adopt')

@app.route('/adopt/bird', methods=['GET'])
def adopt_bird():
    return redirect('/adopt')

if __name__ == '__main__':
    app.run(debug=True)
