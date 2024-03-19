from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate

db = SQLAlchemy()

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    scalemeter = db.Column(db.Float)  # Assuming scalemeter is a floating point number
    movies_description = db.Column(db.Text)
    
    # One-to-Many relationship with Trailers (Assuming a movie can have multiple trailers)
    trailers = db.relationship('Trailer', backref='movie', lazy=True)

class MovieInfo(db.Model):
    __tablename__ = 'movie_info'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)  # Assuming rating is a floating point number
    genre = db.Column(db.String(50))  # Assuming genre can be up to 50 characters
    runtime = db.Column(db.Integer)  # Assuming runtime is in minutes

class Series(db.Model):
    __tablename__ = "series"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    scalemeter = db.Column(db.Float)  # Assuming scalemeter is a floating point number
    series_description = db.Column(db.Text)
    # One-to-Many relationship with Trailers (Assuming a series can have multiple trailers)
    trailers = db.relationship('Trailer', backref='series', lazy=True)

class SeriesInfo(db.Model):
    __tablename__ = 'series_info'

    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)  # Assuming rating is a floating point number
    genre = db.Column(db.String(50))  # Assuming genre can be up to 50 characters
    seasons = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    runtime = db.Column(db.Integer)  # Assuming runtime is in minutes

class TVShows(db.Model):
    __tablename__ = "tv_shows"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    scalemeter = db.Column(db.Float)  # Assuming scalemeter is a floating point number
    tv_shows_description = db.Column(db.Text)
    # One-to-Many relationship with Trailers (Assuming a TV show can have multiple trailers)
    trailers = db.relationship('Trailer', backref='tv_show', lazy=True)

class TVShowsInfo(db.Model):
    __tablename__ = 'tv_shows_info'

    id = db.Column(db.Integer, primary_key=True)
    tv_show_id = db.Column(db.Integer, db.ForeignKey('tv_shows.id'), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)  # Assuming rating is a floating point number
    genre = db.Column(db.String(50))  # Assuming genre can be up to 50 characters
    season = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    runtime = db.Column(db.Integer)  # Assuming runtime is in minutes

class Trailer(db.Model):
    __tablename__ = 'trailers'

    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String(255), nullable=False)  # Assuming URL of YouTube video
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))  # Foreign key to movies table
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))  # Foreign key to series table
    tv_show_id = db.Column(db.Integer, db.ForeignKey('tv_shows.id'))  # Foreign key to tv_shows table
