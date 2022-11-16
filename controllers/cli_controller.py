from flask import Blueprint
from init import db, bcrypt
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

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            first_name='Jerry',
            last_name='Seinfeld',
            email='admin@soty.com',
            password=bcrypt.generate_password_hash('shrinkage').decode('utf-8'),
            is_admin=True
        ),
        User(
            first_name='George',
            last_name='Costanza',
            email='george@soty.com',
            password=bcrypt.generate_password_hash('vandelay').decode('utf-8')
        ),
    ]

    db.session.add_all(users)
    db.session.commit()

    playlists = [
        Playlist(
            playlist_name="Best Songs 2022",
            playlist_year="2022",
            user = users[1]
        )
    ]

    db.session.add_all(playlists)
    db.session.commit()

    songs = [
        Song(
            song_name = "Jackie Down The Line",
            artist = "Fontaines D.C.",
            genre = "Post-Punk",
            album = "Skinty Fia",
            song_year = "2022",
            duration = "243",
            song_link = "https://www.youtube.com/watch?v=3AoOfJP3r40"
        )
    ]

    db.session.add_all(songs)
    db.session.commit()

    # comments = [
    #     Comment(

    #     )
    # ]

    print('Tables seeded')