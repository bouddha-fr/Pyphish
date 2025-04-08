from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(128), nullable=False)  # Le mot de passe est stocké en clair

    def set_password(self, password):
        # On stocke le mot de passe en clair
        self.mot_de_passe = password

    def check_password(self, password):
        # On compare directement les mots de passe en clair
        return self.mot_de_passe == password

    def __repr__(self):
        return f'<Utilisateur {self.email}>'
