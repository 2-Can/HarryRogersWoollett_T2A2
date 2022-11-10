from main import db

class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'

    playlistsongs_id = db.Column(db.Integer, primary_key=True)
    
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'), nullable=False)