from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db' 

db = SQLAlchemy(app)

# Your models go here

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
    parental_guide = db.Column(db.String(50))  # Add this line
    genre = db.Column(db.String(50))
    runtime = db.Column(db.Integer)
    year = db.Column(db.Integer)

   
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
    parental_guide = db.Column(db.String(50))  # Change 'rating' to 'parental_guide'
    genre = db.Column(db.String(50))
    seasons = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
    year = db.Column(db.Integer)

class Trailer(db.Model):
    __tablename__ = 'trailers'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False, default="Trailer")  # Default value added
    video_url = db.Column(db.String(255), nullable=False)  # Assuming URL of YouTube video
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))  # Foreign key to movies table
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))  # Foreign key to series table
