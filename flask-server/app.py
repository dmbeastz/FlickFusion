from flask import Flask, jsonify
from models import db, Movies, MovieInfo, Series, SeriesInfo, Trailer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db'

# Initialize SQLAlchemy instance
db.init_app(app)

# Routes for retrieving data

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movies.query.all()
    return jsonify([movie.serialize() for movie in movies])

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movies.query.get(movie_id)
    if movie:
        return jsonify(movie.serialize())
    else:
        return jsonify({"error": "Movie not found"}), 404

@app.route('/series', methods=['GET'])
def get_series():
    series = Series.query.all()
    return jsonify([series_item.serialize() for series_item in series])

@app.route('/series/<int:series_id>', methods=['GET'])
def get_series_info_by_id_endpoint(series_id):
    series = Series.query.get(series_id)
    if series:
        return jsonify(series.serialize())
    else:
        return jsonify({"error": "Series not found"}), 404

@app.route('/movieinfo', methods=['GET'])
def get_all_movie_info():
    movie_info = MovieInfo.query.all()
    return jsonify([info.serialize() for info in movie_info])

@app.route('/movieinfo/<int:movie_id>', methods=['GET'])
def get_movie_info_by_id(movie_id):
    movie_info = MovieInfo.query.filter_by(movie_id=movie_id).first()
    if movie_info:
        return jsonify(movie_info.serialize())
    else:
        return jsonify({"error": "Movie info not found"}), 404

@app.route('/seriesinfo', methods=['GET'])
def get_all_series_info():
    series_info = SeriesInfo.query.all()
    return jsonify([info.serialize() for info in series_info])

@app.route('/seriesinfo/<int:series_id>', methods=['GET'])
def get_series_info_by_id(series_id):
    series_info = SeriesInfo.query.filter_by(series_id=series_id).first()
    if series_info:
        return jsonify(series_info.serialize())
    else:
        return jsonify({"error": "Series info not found"}), 404

@app.route('/trailers', methods=['GET'])
def get_trailers():
    trailers = Trailer.query.all()
    return jsonify([trailer.serialize() for trailer in trailers])

@app.route('/trailers/<int:trailer_id>', methods=['GET'])
def get_trailer(trailer_id):
    trailer = Trailer.query.get(trailer_id)
    if trailer:
        return jsonify(trailer.serialize())
    else:
        return jsonify({"error": "Trailer not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
