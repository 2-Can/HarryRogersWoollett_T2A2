from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required
from models.song import Song, SongSchema
from controllers.auth_controller import authorize

songs_bp = Blueprint('songs', __name__, url_prefix='/songs' )

# Get all songs
@songs_bp.route('/')
@jwt_required()
def get_all_songs():
    # Get a list of all songs
    stmt = db.select(Song)
    songs = db.session.scalars(stmt)
    return SongSchema(many=True).dump(songs)

# Get one song
@songs_bp.route('/<int:song_id>/')
@jwt_required()
def get_one_song(song_id):
    stmt = db.select(Song).filter_by(song_id=song_id)
    song = db.session.scalar(stmt)
    if song:
        return SongSchema().dump(song)
    else:
        return {'error': f'Song not found with id {song_id}'}, 404


# Create song
@songs_bp.route('/create/', methods=['POST'])
@jwt_required()
def create_song():
    # Create a new song entry
    data = SongSchema().load(request.json)

    song = Song(
        song_name = data['song_name'],
        artist = data['artist'],
        genre = data['genre'],
        album = data['album'],
        song_year = data['song_year'],
        duration = data['duration'],
        song_link = data['song_link'],
    )
    db.session.add(song)
    db.session.commit()

    return SongSchema().dump(song), 201

# Update song
@songs_bp.route('/<int:song_id>/', methods=['PUT', 'PATCH'])
@jwt_required()
# Update a song's details
def update_song(song_id):
    stmt = db.select(Song).filter_by(song_id=song_id)
    song = db.session.scalar(stmt)
    if song:
        song.song_name = request.json.get('song_name') or song.song_name
        song.artist = request.json.get('artist') or song.artist
        song.genre = request.json.get('genre') or song.genre
        song.album = request.json.get('album') or song.album
        song.song_year = request.json.get('song_year') or song.song_year
        song.duration = request.json.get('duration') or song.duration
        song.song_link = request.json.get('song_link') or song.song_link
        db.session.commit()
        return SongSchema().dump(song)
    else:
        return {'error': f'Song not found with id {song_id}'}, 404

# Delete Song
@songs_bp.route('/<int:song_id>', methods=['DELETE'])
@jwt_required()
def delete_one_song(song_id):
    # Delete a Song
    authorize()

    stmt = db.select(Song).filter_by(song_id=song_id)
    song = db.session.scalar(stmt)
    if song:
        db.session.delete(song)
        db.session.commit()
        return {'message': f"Song '{song.song_name}' deleted successfully"}
    else:
        return {'error': f'Song not found with Song ID {song_id}'}, 404
