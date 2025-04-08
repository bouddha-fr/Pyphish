from flask import Flask, render_template, request, redirect, url_for, flash, session
from src.app.models import Utilisateur
from werkzeug.security import check_password_hash

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

        if utilisateur and check_password_hash(utilisateur.mot_de_passe, mot_de_passe):
            # Utilisateur authentifié, on démarre une session
            session["utilisateur_id"] = utilisateur.id
            flash("Connexion réussie!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Email ou mot de passe incorrect", "danger")
            return redirect(url_for("connexion"))

    @app.route("/dashboard")
    def dashboard():
        if "utilisateur_id" not in session:
            return redirect(url_for("connexion"))
        return render_template('pydashboard.html')
