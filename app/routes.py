from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Hello, Flask CI/CD! web app made cheap and fast with Flask!!!!! I made this using jenkins"
