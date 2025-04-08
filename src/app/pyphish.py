from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.app.routes.routes import register_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://user:password@localhost:3306/pyphish'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'motdepasse'

db = SQLAlchemy(app)

register_routes(app, db)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
