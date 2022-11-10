from flask import Blueprint

songs_bp = Blueprint('songs', __name__, url_prefix='/songs' )