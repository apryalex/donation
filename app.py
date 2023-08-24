from flask import Flask, render_template, request, redirect, url_for
from data import enregistrer_promesse, lire_promesses, lire_promesse_par_id


app = Flask(__name__)


# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Page de promesse de don
@app.route('/promesse_don', methods=['GET', 'POST'])
def promesse_don():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']
        email = request.form['email']
        somme_promise = request.form['somme_promise']

        # Enregistrement des informations dans la base de données
        enregistrer_promesse(nom, prenom, adresse, email, somme_promise)

        return redirect(url_for('promesses_enregistrees'))

    return render_template('promesse_don.html')

# Page des promesses enregistrées
@app.route('/promesses_enregistrees')
def promesses_enregistrees():
    # Récupération des promesses de don depuis la base de données
    promesses = lire_promesses()

    return render_template('promesses_enregistrees.html', promesses=promesses)

if __name__ == '__main__':
    app.run(debug=True)
