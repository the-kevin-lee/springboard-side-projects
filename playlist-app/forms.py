"""Forms for playlist app."""

from wtforms import SelectField, TextAreaField, SubmitField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Playlist Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Playlist Description', validator=[Length(max=255)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Song Title', validators=[DataRequired(), Length(min=2,max=100)])
    artist = StringField('Artist Name', validators = [DataRequired(), Length(min=2,max=100)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
