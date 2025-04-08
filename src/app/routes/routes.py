from flask import Flask, render_template, request, redirect, url_for, flash, session
from src.app.models import User
from werkzeug.security import check_password_hash
from src.app import db

def register_routes(app: Flask, db):
    @app.route("/")
    def hello_world():
        return render_template('index.html')

    @app.route("/connexion")
    def connexion():
        return render_template('pyconnexion.html')

    @app.route("/login", methods=["POST"])
    def login():
        username = request.form.get("username")
        password = request.form.get("password")

        # Chercher l'utilisateur dans la base de données
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # Utilisateur authentifié, on démarre une session
            session["user_id"] = user.id
            flash("Connexion réussie!", "success")
            return redirect(url_for("dashboard"))  # Redirige vers une page protégée, comme un dashboard
        else:
            flash("Nom d'utilisateur ou mot de passe incorrect", "danger")
            return redirect(url_for("connexion"))

    @app.route("/dashboard")
    def dashboard():
        if "user_id" not in session:
            return redirect(url_for("connexion"))  # Redirige si l'utilisateur n'est pas connecté
        return render_template('dashboard.html')  # Page protégée accessible après connexion
