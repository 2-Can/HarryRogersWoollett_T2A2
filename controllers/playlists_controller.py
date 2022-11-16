from flask import Blueprint
# from main import db

playlists_bp = Blueprint('playlists', __name__, url_prefix='/playlists' )

@playlists_bp.route('')
def test():
    return 'playlists route'

@playlists_bp.route('/secondary')
def secondary():
    return 'playlists secondary route'
