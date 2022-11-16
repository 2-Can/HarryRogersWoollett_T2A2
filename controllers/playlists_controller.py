from flask import Blueprint
from init import db

playlists_bp = Blueprint('playlists', __name__, url_prefix='/playlists' )

@playlists_bp.route('/')
def get_all_playlists():
    return 'playlists route'

@playlists_bp.route('/secondary')
def secondary():
    return 'playlists secondary route'
