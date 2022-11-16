from flask import Blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from init import db
# from models.playlist import PlaylistSchema

playlists_bp = Blueprint('playlists', __name__, url_prefix='/playlists' )

# @playlists_bp.route('/')
# @jwt_required
# def get_all_playlists():
#     playlists = db.session.scalars(stmt)
#     return PlaylistSchema(many=True).dump(playlists)

# @playlists_bp.route('/secondary')
# def secondary():
#     return 'playlists secondary route'
