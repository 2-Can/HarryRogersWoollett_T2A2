from marshmallow import fields
from init import db, ma

class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'

    playlistsongs_id = db.Column(db.Integer, primary_key=True)

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'), nullable=False)

    playlist = db.relationship('Playlist', back_populates='playlist_songs')

class PlaylistSongSchema(ma.Schema):
    playlists = fields.List(fields.Nested('PlaylistSchema'))

    class Meta:
        fields = ('playlistsongs_id', 'playlist_id')
        ordered = True
    