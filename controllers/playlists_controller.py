from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.playlist import Playlist, PlaylistSchema
from controllers.auth_controller import authorize
from sqlalchemy.exc import IntegrityError

playlists_bp = Blueprint('playlists', __name__, url_prefix='/playlists' )

@playlists_bp.route('/')
@jwt_required()
def get_all_playlists():
    # Get a list of all playlists
    stmt = db.select(Playlist)
    playlists = db.session.scalars(stmt)
    return PlaylistSchema(many=True).dump(playlists)


@playlists_bp.route('/create/', methods=['POST'])
@jwt_required()
def create_playlist():
    # Create a new Playlist
    data = PlaylistSchema().load(request.json)

    playlist = Playlist(
        playlist_name = data['playlist_name'],
        playlist_year = data['playlist_year'],
        user_id = get_jwt_identity()
    )
    db.session.add(playlist)
    db.session.commit()

    return PlaylistSchema().dump(playlist), 201


@playlists_bp.route('/<int:playlist_id>', methods=['DELETE'])
@jwt_required()
def delete_one_playlist(playlist_id):
    # Delete a Playlist
    authorize()

    stmt = db.select(Playlist).filter_by(playlist_id=playlist_id)
    playlist = db.session.scalar(stmt)
    if playlist:
        db.session.delete(playlist)
        db.session.commit()
        return {'message': f"Playlist '{playlist.playlist_name}' deleted successfully"}
    else:
        return {'error': f'Playlist not found with Playlist ID {playlist_id}'}, 404


@playlists_bp.route('/<int:playlist_id>/', methods=['PUT', 'PATCH'])
@jwt_required()
# Update a playlist's details
def update_playlist(playlist_id):
    stmt = db.select(Playlist).filter_by(playlist_id=playlist_id)
    playlist = db.session.scalar(stmt)
    if playlist:
        playlist.playlist_name = request.json.get('playlist_name') or playlist.playlist_name
        playlist.playlist_year = request.json.get('playlist_year') or playlist.playlist_year
        db.session.commit()      
        return PlaylistSchema().dump(playlist)
    else:
        return {'error': f'Playlist not found with id {playlist_id}'}, 404