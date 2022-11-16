from marshmallow import fields
from init import db, ma

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    date = db.Column(db.Date)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'), nullable=False)

    user = db.relationship('User', back_populates='comments')
    playlist = db.relationship('Playlist', back_populates='comments')

class CommentSchema(ma.Schema):
    playlists = fields.List(fields.Nested('PlaylistSchema', exclude=['user']))

    class Meta:
        fields = ('comment_id', 'message', 'date')