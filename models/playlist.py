from main import db

class Playlist(db.Model):
    __tablename__ = 'playlists'

    playlist_id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.Text)
    playlist_year = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
