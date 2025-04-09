from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin', 'user'), nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    campagnes = db.relationship('Campagne', backref='utilisateur', lazy=True)

    def set_password(self, password):
        self.mot_de_passe = password

    def check_password(self, password):
        return self.mot_de_passe == password

    def __repr__(self):
        return f'<Utilisateur {self.email}>'


class TemplateSite(db.Model):
    __tablename__ = 'template_site'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    url_redirection = db.Column(db.String(255))

    cibles = db.relationship('Cible', backref='template', lazy=True)
    campagnes = db.relationship('Campagne', backref='template', lazy=True)

    def __repr__(self):
        return f'<TemplateSite {self.nom}>'


class Cible(db.Model):
    __tablename__ = 'cible'

    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(100))
    nom = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255))
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    site_id = db.Column(db.Integer, db.ForeignKey('template_site.id'), nullable=True)

    def __repr__(self):
        return f'<Cible {self.email}>'


class Campagne(db.Model):
    __tablename__ = 'campagne'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    date_lancement = db.Column(db.DateTime, default=datetime.utcnow)

    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=True)
    template_id = db.Column(db.Integer, db.ForeignKey('template_site.id'), nullable=True)

    def __repr__(self):
        return f'<Campagne {self.nom}>'
