from flask import Blueprint
from flask_jwt_extended import jwt_required
from init import db
from models.playlist import Playlist, PlaylistSchema

playlists_bp = Blueprint('playlists', __name__, url_prefix='/playlists' )

@playlists_bp.route('/')
@jwt_required()
def get_all_playlists():
    stmt = db.select(Playlist)
    playlists = db.session.scalars(stmt)
    return PlaylistSchema(many=True).dump(playlists)

@playlists_bp.route('/secondary')
def secondary():
    return 'playlists secondary route'
