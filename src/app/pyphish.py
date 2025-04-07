from flask import Flask
from src.app.routes.routes import register_routes

app = Flask(__name__)
register_routes(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
