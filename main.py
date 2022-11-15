import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from init import db, ma, bcrypt, jwt
from flask import Flask
from controllers.playlists_controller import playlists_bp
from controllers.cli_controller import db_commands

def create_app():
    app = Flask(__name__)

    app.config ['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(playlists_bp)
    app.register_blueprint(db_commands)

    return app