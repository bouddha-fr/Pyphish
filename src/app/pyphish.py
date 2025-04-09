from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.routes import register_routes
from app.models import db  # Si db est défini dans models, on l'importera ici

app = Flask(__name__)

# Configuration de l'application Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:Motdepasse@172.16.160.132:3306/pyphish'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Motdepasse'

# Initialisation de db avec l'application via init_app
db.init_app(app)

# Enregistrement des routes
register_routes(app, db)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
