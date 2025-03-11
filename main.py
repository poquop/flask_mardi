from flask import Flask, request, redirect, url_for

app = Flask(__name__)

specialites_lycee = [
    "Mathématiques",
    "Physique-Chimie",
    "Sciences de la Vie et de la Terre (SVT)",
    "Numérique et Sciences Informatiques (NSI)",
    "Sciences de l'Ingénieur (SI)",
    "Sciences Économiques et Sociales (SES)",
    "Humanités, Littérature et Philosophie (HLP)",
    "Histoire-Géographie, Géopolitique et Sciences Politiques (HGGSP)",
    "Langues, Littératures et Cultures Étrangères (LLCE) - Anglais",
    "Langues, Littératures et Cultures Étrangères (LLCE) - Espagnol",
    "Langues, Littératures et Cultures Étrangères (LLCE) - Allemand",
    "Langues, Littératures et Cultures Étrangères (LLCE) - Italien",
    "Langues, Littératures et Cultures Étrangères (LLCE) - Chinois",
    "Langues et Cultures de l'Antiquité (LCA) - Latin",
    "Langues et Cultures de l'Antiquité (LCA) - Grec",
    "Arts Plastiques",
    "Musique",
    "Théâtre",
    "Cinéma-Audiovisuel",
    "Droits et Grands Enjeux du Monde Contemporain (DGEMC)",
    "Biotechnologies",
    "Sciences et Techniques Sanitaires et Sociales (ST2S)",
    "Écologie, Agronomie et Territoires (EAT)",
    "Management et Gestion",
    "Éducation Physique, Pratiques et Culture Sportive (EPPCS)",
    "Géopolitique et Sciences Sociales",
    "Informatique et Création Numérique (ICN)",
    "Ingénierie, Innovation et Développement Durable",
    "Enseignement Technologique en Langue Étrangère (ETLV)",
    "Santé et Social",
    "Sciences de Laboratoire",
    "Sciences des Matériaux et Structures",
    "Sciences du Numérique",
    "Géosciences et Environnement",
    "Philosophie et Sciences Humaines",
    "Mathématiques Complémentaires",
    "Mathématiques Expertes"
]

options_lycee = [
    "Latin",
    "Grec",
    "Section Européenne (Anglais, Espagnol, Allemand, Italien, etc.)",
    "Section Internationale (Anglais, Espagnol, Allemand, Chinois, etc.)",
    "Section Binationale (ABIBAC, BACHIBAC, ESABAC)",
    "Langue Vivante 3 (Chinois, Russe, Japonais, Arabe, Portugais, etc.)",
    "Arts Plastiques",
    "Cinéma-Audiovisuel",
    "Musique",
    "Théâtre",
    "Danse",
    "Éducation Physique et Sportive (EPS) renforcée",
    "Sport (Section Sportive Scolaire)",
    "Hip-Hop",
    "Chant choral",
    "Orchestre",
    "Échecs",
    "Informatique et Création Numérique (ICN)",
    "Création et Innovation Technologique (CIT)",
    "Méthodes et Pratiques Scientifiques (MPS)",
    "Sciences et Laboratoire",
    "Technologie et Sciences de l'Ingénieur (TSI)",
    "Management et Gestion",
    "Pratiques Sociales et Culturelles",
    "Sciences Politiques et Sociales",
    "Agronomie et Développement Durable",
    "Développement Durable et Environnement",
    "Écologie",
    "Citoyenneté et Droits de l'Homme",
    "Économie et Monde Contemporain",
    "Humanités et Philosophie",
    "Langue des Signes Française (LSF)",
    "Histoire des Arts",
    "Architecture et Patrimoine",
    "Patrimoine et Civilisation",
    "Astronomie",
    "Robotique",
    "Aéronautique (Brevet d'Initiation Aéronautique - BIA)",
    "Énergie et Développement Durable",
    "Intelligence Artificielle et Data Science",
    "Métiers de la Sécurité et Défense",
    "Secourisme",
    "Culture et Patrimoine",
    "Journalisme et Médias",
    "Entrepreneuriat",
    "Arts du Cirque",
    "Éthique et Société",
    "Communication et Prise de Parole",
    "Économie Sociale et Solidaire",
    "Cuisine et Gastronomie",
    "Hôtellerie et Restauration",
    "Tourisme",
    "Langues et Cultures Régionales (Breton, Basque, Corse, Occitan, etc.)",
    "Expérimentation et Recherche en Sciences",
    "Neurosciences et Cognition",
    "Programmation et Algorithmique",
    "Cyber-Sécurité",
    "Cryptographie et Mathématiques Appliquées"
]

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

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html', specialites_lycee=specialites_lycee, options_lycee=options_lycee)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    return request.form

app.run(host='localhost', port=8000)

