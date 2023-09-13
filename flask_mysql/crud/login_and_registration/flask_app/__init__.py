from flask import Flask
app = Flask(__name__)
app.secret_key = 'this is my security key'
import flask_app.controllers
import flask_app.models
