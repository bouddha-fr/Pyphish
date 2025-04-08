from flask import Flask, render_template

app = Flask(__name__)

def register_routes(app: Flask):
    @app.route("/")
    def hello_world():
        return render_template('index.html')
    @app.route("/connexion")
    def dashboard():
        return render_template('pyconnexion.html')