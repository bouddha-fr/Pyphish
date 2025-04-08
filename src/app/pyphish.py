from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.app.routes.routes import register_routes
from src.app.models import db  # Si db est défini dans models, on l'importera ici

app = Flask(__name__)

# Configuration de l'application Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:Motdepasse@172.16.27.135:3306/pyphish'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Motdepasse'

# Initialisation de db avec l'application via init_app
db.init_app(app)

# Enregistrement des routes
register_routes(app, db)

if __name__ == "__main__":
    app.run(host="172.16.27.135", port=8000, debug=True)
