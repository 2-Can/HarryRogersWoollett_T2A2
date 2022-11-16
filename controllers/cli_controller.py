from flask import Blueprint
from init import db, bcrypt
from datetime import date
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
        ),
        Song(
            song_name = "Come On Let's Go",
            artist = "Tyler The Creator",
            genre = "Hip-Hop",
            album = "I Know Nigo!",
            song_year = "2022",
            duration = "200",
            song_link = "https://www.youtube.com/watch?v=zuuPitOYNY4"
        ),
        Song(
            song_name = "SAOKO",
            artist = "Rosalia",
            genre = "Reggaeton",
            album = "Motomami",
            song_year = "2022",
            duration = "137",
            song_link = "https://www.youtube.com/watch?v=ApNQX6fVWQ4"
        ),
        Song(
            song_name = "The Smoke",
            artist = "The Smile",
            genre = "Alternative Rock",
            album = "A Light For Attracting Attention",
            song_year = "2022",
            duration = "220",
            song_link = "https://www.youtube.com/watch?v=theOkhAWs2s"
        ),
        Song(
            song_name = "Zipcodes",
            artist = "Joey Bada$$",
            genre = "Hip-Hop",
            album = "2000",
            song_year = "2022",
            duration = "265",
            song_link = "https://www.youtube.com/watch?v=Fy3070QgHV0"
        ),
        Song(
            song_name = "Ain't No Thief",
            artist = "Viagra Boys",
            genre = "Post-Punk",
            album = "Cave World",
            song_year = "2022",
            duration = "239",
            song_link = "https://www.youtube.com/watch?v=EAJLz6rbUSg"
        ),
        Song(
            song_name = "Hot Girl",
            artist = "Charli XCX",
            genre = "Pop",
            album = "Bodies Bodies Bodies",
            song_year = "2022",
            duration = "156",
            song_link = "https://www.youtube.com/watch?v=vKIU3Q5oiMg"
        ),
        Song(
            song_name = "Cutie",
            artist = "Shanti Celeste",
            genre = "House",
            album = "HES041",
            song_year = "2022",
            duration = "386",
            song_link = "https://www.youtube.com/watch?v=mYWNROkV9uc"
        ),
        Song(
            song_name = "Pledge Drive",
            artist = "Cheekface",
            genre = "Alternative Rock",
            album = "Too Much To Ask",
            song_year = "2022",
            duration = "164",
            song_link = "https://www.youtube.com/watch?v=lOSXqWTvygY"
        ),
        Song(
            song_name = "All You Do",
            artist = "Magdalena Bay",
            genre = "Pop",
            album = "Mercurial World Deluxe",
            song_year = "2022",
            duration = "268",
            song_link = "https://www.youtube.com/watch?v=wxaJ8aiURgU"
        ),
    ]

    db.session.add_all(songs)
    db.session.commit()

    comments = [
        Comment(
            message = 'this playlist sucks',
            user = users[1],
            playlist = playlists[0],
            date = date.today()
        )
    ]

    db.session.add_all(comments)
    db.session.commit()


    print('Tables seeded')