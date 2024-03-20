import random
from flask import Flask
from models import db, Movies, MovieInfo, Series, SeriesInfo, TVShows, TVShowsInfo, Trailer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db'
db.init_app(app)

with app.app_context():
    print("Seeding Movies")

    movies_data = [
        {"title": "The Amazing Spider-Man", "stars": 5, "year": 2014, "poster": "https://i.pinimg.com/564x/c5/7e/b6/c57eb61ecc25097a4a3682238efe3d5d.jpg"},
        {"title": "Fast and Furious 6", "stars": 4, "year": 2013, "poster": "https://i.pinimg.com/564x/19/2a/66/192a66022855d80ea8f95c930382f914.jpg"},
        {"title": "Avengers: Infinity War", "stars": 4.5, "year": 2018, "poster": "https://i.pinimg.com/564x/d0/d2/a5/d0d2a5365c6de34873d5ae340574a6f6.jpg"},
        {"title": "Avengers: Endgame", "stars": 4.8, "year": 2019, "poster": "https://i.pinimg.com/564x/fd/0a/95/fd0a95013300f069d2955a4e5f911c24.jpg"},
        {"title": "Captain America: The Winter Soldier", "stars": 4.6, "year": 2014, "poster": "https://i.pinimg.com/564x/d3/a3/41/d3a34185e85d1ee01de8f4686553c1c9.jpg"}
    ]

    for movie_data in movies_data:
        movie = Movies(title=movie_data['title'], stars=movie_data['stars'], year=movie_data['year'], poster=movie_data['poster'])
        db.session.add(movie)

    db.session.commit()

    print("Movies seeded successfully")

print("Seeding Series")

series_data = [
    {"title": "Breaking Bad", "stars": 4.9, "year": 2008, "poster": "https://i.pinimg.com/564x/37/62/75/37627587496965efcc0ae42ac9dff525.jpg"},
    {"title": "Game of Thrones", "stars": 4.7, "year": 2011, "poster": "https://i.pinimg.com/564x/51/1a/63/511a6304f9e351f084ec9b540ccf3da9.jpg"},
    {"title": "Stranger Things", "stars": 4.6, "year": 2016, "poster": "https://i.pinimg.com/564x/91/9b/55/919b55a36c4917c565aad3b16b3750e5.jpg"},
    {"title": "The Crown", "stars": 4.5, "year": 2016, "poster": "https://i.pinimg.com/564x/75/c3/19/75c31924c94311120c4554cda5d6d378.jpg"},
    {"title": "The Mandalorian", "stars": 4.8, "year": 2019, "poster": "https://i.pinimg.com/564x/67/33/66/673366f7843e0c2fbfdbf23bdde30c4a.jpg"},
    {"title": "Friends", "stars": 4.8, "year": 1994, "poster": "https://i.pinimg.com/564x/15/c4/da/15c4da03bc524af9b91ee676519b12b1.jpg"},
    {"title": "The Office (US)", "stars": 4.7, "year": 2005, "poster": "https://i.pinimg.com/564x/85/3e/f1/853ef165a539dcbb4eaa217cbb61a2d3.jpg"}
]

for series_data_item in series_data:
    series = Series.query.filter_by(title=series_data_item['title']).first()
    if not series:
        series = Series(title=series_data_item['title'], stars=series_data_item['stars'], year=series_data_item['year'], poster=series_data_item['poster'])
        db.session.add(series)

db.session.commit()

print("Series seeded successfully")
