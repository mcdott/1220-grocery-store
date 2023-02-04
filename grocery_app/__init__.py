from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from .models import User
from grocery_app.extensions import app, db

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

bcrypt = Bcrypt(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
