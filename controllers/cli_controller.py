from flask import Blueprint
from init import db
from models.user import User
from models.playlist import Playlist
from models.song import Song
from models.comment import Comment
from models.playlistsong import PlaylistSong

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")