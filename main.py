import os
from init import db, ma, bcrypt, jwt
from flask import Flask
from controllers.playlists_controller import playlists_bp
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp

def create_app():
    app = Flask(__name__)

    app.config ['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(playlists_bp)
    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)

    return app