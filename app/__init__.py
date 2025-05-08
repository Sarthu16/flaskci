# app/__init__.py
from flask import Flask
from .routes import main  # Assuming your blueprint is named 'main'

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
