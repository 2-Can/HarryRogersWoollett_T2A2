import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from controllers.playlists_controller import playlists_bp

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') 

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(playlists_bp)

    return app