from flask import Blueprint
from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.song import Song, SongSchema

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

# Create song

# Update song

# Delete Song

