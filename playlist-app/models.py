"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__="playlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(235))     


class Song(db.Model):
    """Song."""
    __tablename__='songs'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    artist=db.Column(db.String(100), nullable=False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename_='playlist_songs'

    playlist_id = db.Column(db.Integer,db.ForeignKey('playlists.id'),primary_key=True)
    song_id = db.Column(db.Integer,db.ForeignKey('songs.id'), primary_key=True)
    #Relationships
    playlist = db.relationship('Playlist', backref=db.backref('playlist_songs', cascade='all, delete-orphan'))
    song = db.relationship('Song', backref=db.backref('playlist_songs', cascade='all, delete-orphan'))
   


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
