from init import db, ma
from marshmallow import fields


class Playlist(db.Model):
    __tablename__ = 'playlists'

    playlist_id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.Text)
    playlist_year = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship('User', back_populates='playlist')
    comments = db.relationship('Comment', back_populates='playlist', cascade='all, delete' )

# class PlaylistSchema(ma.Schema):
