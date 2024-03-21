from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db' 


db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

# Your models and routes go here
db = SQLAlchemy()

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    stars = db.Column(db.Float)  # Assuming stars represent the quality/liking of the movie
    year = db.Column(db.Integer)  # Year of the movie
    poster = db.Column(db.String(255))  # Assuming the poster is stored as a URL to an image
    # One-to-Many relationship with Trailers (Assuming a movie can have multiple trailers)
    trailers = db.relationship('Trailer', backref='movie', lazy=True)

class MovieInfo(db.Model):
    __tablename__ = 'movie_info'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.String(50))  # Changed to String for parental guide rating
    genre = db.Column(db.String(50))  # Assuming genre can be up to 50 characters
    runtime = db.Column(db.Integer)  # Assuming runtime is in minutes
    year = db.Column(db.Integer)  # Year of the movie

class Series(db.Model):
    __tablename__ = "series"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    stars = db.Column(db.Float)  # Assuming stars represent the quality/liking of the series
    year = db.Column(db.Integer)  # Year of the series
    poster = db.Column(db.String(255))  # Assuming the poster is stored as a URL to an image
    # One-to-Many relationship with Trailers (Assuming a series can have multiple trailers)
    trailers = db.relationship('Trailer', backref='series', lazy=True)

class SeriesInfo(db.Model):
    __tablename__ = 'series_info'

    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.String(50))  # Changed to String for parental guide rating
    genre = db.Column(db.String(50))  # Assuming genre can be up to 50 characters
    seasons = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    runtime = db.Column(db.Integer)  # Assuming runtime is in minutes
    year = db.Column(db.Integer)  # Year of the series

class Trailer(db.Model):
    __tablename__ = 'trailers'

    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String(255), nullable=False)  # Assuming URL of YouTube video
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))  # Foreign key to movies table
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))  # Foreign key to series table

