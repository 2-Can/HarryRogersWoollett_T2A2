from marshmallow import fields
from init import db, ma


class Playlist(db.Model):
    __tablename__ = 'playlists'

    playlist_id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.Text)
    playlist_year = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship('User', back_populates='playlists')
    comments = db.relationship('Comment', back_populates='playlist', cascade='all, delete' )
    playlist_songs = db.relationship('PlaylistSong', back_populates='playlist', cascade='all, delete')


class PlaylistSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['first_name', 'last_name', 'email'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['playlist_id']))
    playlist_songs = fields.List(fields.Nested('PlaylistSongSchema', exclude=['playlist_id']))

    class Meta:
        fields = ('playlist_id', 'playlist_name', 'playlist_year', 'user', 'playlist_songs', 'comments')
        ordered = True
    