from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db' 

db = SQLAlchemy(app)

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    stars = db.Column(db.Float)
    year = db.Column(db.Integer)
    poster = db.Column(db.String(255))
    trailers = db.relationship('Trailer', backref='movie', lazy=True)
    # Add relationship with MovieInfo
    info = db.relationship('MovieInfo', backref='movie', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'stars': self.stars,
            'year': self.year,
            'poster': self.poster
        }

class MovieInfo(db.Model):
    __tablename__ = 'movie_info'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    description = db.Column(db.Text)
    parental_guide = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    runtime = db.Column(db.Integer)
    year = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'description': self.description,
            'parental_guide': self.parental_guide,
            'genre': self.genre,
            'runtime': self.runtime,
            'year': self.year
        }

class Series(db.Model):
    __tablename__ = "series"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    stars = db.Column(db.Float)
    year = db.Column(db.Integer)
    poster = db.Column(db.String(255))
    trailers = db.relationship('Trailer', backref='series', lazy=True)
    # Add relationship with SeriesInfo
    info = db.relationship('SeriesInfo', backref='series', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'stars': self.stars,
            'year': self.year,
            'poster': self.poster
        }

class SeriesInfo(db.Model):
    __tablename__ = 'series_info'

    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)
    description = db.Column(db.Text)
    parental_guide = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    seasons = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
    year = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'series_id': self.series_id,
            'description': self.description,
            'parental_guide': self.parental_guide,
            'genre': self.genre,
            'seasons': self.seasons,
            'episodes': self.episodes,
            'runtime': self.runtime,
            'year': self.year
        }

class Trailer(db.Model):
    __tablename__ = 'trailers'

    id = db.Column(db.Integer, primary_key=True)
    trailer_title = db.Column(db.String(140), nullable=False, default="Trailer")
    video_url = db.Column(db.String(255), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))

    def serialize(self):
        return {
            'id': self.id,
            'trailer_title': self.trailer_title,  # Corrected attribute name
            'video_url': self.video_url
        }