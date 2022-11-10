from main import db

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    date = db.Column(db.Date)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlists_id'), nullable=False)