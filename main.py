from flask import Flask, render_template

app = Flask(__name__)

gestionnaire = {
    'TFerragu': {
        'nom': 'Ferragu',
        'prenom': 'Thomas',
        'age': 25,
        'notes': {
            'Maths': [
                12,
                14
            ],
            'SES': [
                14,
                17,
                15
            ],
            'Physique': [
                20,
                20
            ]
        }
    },
    'BLéa': {
        'nom': 'Léa',
        'prenom': 'BARBERON',
        'age': 25,
        'notes': {
            'Maths': [
                20,
                14
            ],
            'NSI': [
                20,
                14,
                20,
                20
            ],
            'Physique': []
        }
    }
}

@app.route("/")
def index():
    return render_template(
        'index.html',
        dico = gestionnaire
    )

@app.route("/eleve/<identifier>")
def eleve(identifier):
    return render_template(
        'eleve.html',
        t_eleve = gestionnaire[identifier]
    )

app.run(host='localhost', port=8000)

