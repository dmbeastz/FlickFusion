import random
from flask import Flask
from models import db, Movies, MovieInfo, Series, SeriesInfo, Trailer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db'
db.init_app(app)

def seed_data():
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

        print("Seeding Movie_Info")

        movies_info_data = [
            {"title": "The Amazing Spider-Man", "description": "After Peter Parker is bitten by a genetically altered spider, he gains newfound, spider-like powers and ventures out to save the city from the machinations of a mysterious reptilian foe.", "parental_guide": "PG-13", "genre": "Action", "runtime": 140, "year": 2012},
            {"title": "Fast and Furious 6", "description": "Hobbs has Dominic and Brian reassemble their crew to take down a team of mercenaries: Dominic unexpectedly gets sidetracked with facing his presumed deceased girlfriend, Letty.", "parental_guide": "PG-13", "genre": "Action", "runtime": 130, "year": 2013},
            {"title": "Avengers: Infinity War", "description": "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.", "parental_guide": "PG-13", "genre": "Action", "runtime": 150, "year": 2018},
            {"title": "Avengers: Endgame", "description": "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.", "parental_guide": "PG-13", "genre": "Action", "runtime": 160, "year": 2019},
            {"title": "Captain America: The Winter Soldier", "description": "As Steve Rogers struggles to embrace his role in the modern world, he teams up with a fellow Avenger and S.H.I.E.L.D agent, Black Widow, to battle a new threat from history: an assassin known as the Winter Soldier.", "parental_guide": "PG-13", "genre": "Action", "runtime": 135, "year": 2014}
        ]

        for movie_info_data in movies_info_data:
            movie = Movies.query.filter_by(title=movie_info_data['title']).first()
            if movie:
                movie_info = MovieInfo(movie_id=movie.id, description=movie_info_data['description'], parental_guide=movie_info_data['parental_guide'], genre=movie_info_data['genre'], runtime=movie_info_data['runtime'], year=movie_info_data['year'])
                db.session.add(movie_info)

        db.session.commit()
        print("Movie_Info seeded successfully")

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

        print("Seeding Series_Info")

        series_info_data = [
            {"title": "Breaking Bad", "description": "A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a former student in order to secure his family's future.", "parental_guide": "TV-MA", "genre": "Drama", "seasons": 5, "episodes": 62, "runtime": 50, "year": 2008},
            {"title": "Game of Thrones", "description": "Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for a millennia.", "parental_guide": "TV-MA", "genre": "Fantasy", "seasons": 8, "episodes": 73, "runtime": 60, "year": 2011},
            {"title": "Stranger Things", "description": "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl.", "parental_guide": "TV-14", "genre": "Horror", "seasons": 3, "episodes": 25, "runtime": 55, "year": 2016},
            {"title": "The Crown", "description": "Follows the political rivalries and romances of Queen Elizabeth II's reign and the events that shaped Britain for the second half of the 20th century.", "parental_guide": "TV-MA", "genre": "Drama", "seasons": 4, "episodes": 40, "runtime": 55, "year": 2016},
            {"title": "The Mandalorian", "description": "The travels of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.", "parental_guide": "TV-14", "genre": "Sci-Fi", "seasons": 2, "episodes": 16, "runtime": 45, "year": 2019},
            {"title": "Friends", "description": "Follows the personal and professional lives of six twenty to thirty year-old friends living in the Manhattan borough of New York City.", "parental_guide": "TV-14", "genre": "Comedy", "seasons": 10, "episodes": 236}
        ]

        for series_info_data_item in series_info_data:
            series = Series.query.filter_by(title=series_info_data_item['title']).first()
            if series:
                description = series_info_data_item.get('description', '')
                parental_guide = series_info_data_item.get('parental_guide', '')
                genre = series_info_data_item.get('genre', '')
                seasons = series_info_data_item.get('seasons', 0)
                episodes = series_info_data_item.get('episodes', 0)
                runtime = series_info_data_item.get('runtime', 0)  # Default value if key is missing
                year = series_info_data_item.get('year', 0)

                series_info = SeriesInfo(
                    series_id=series.id,
                    description=description,
                    parental_guide=parental_guide,
                    genre=genre,
                    seasons=seasons,
                    episodes=episodes,
                    runtime=runtime,
                    year=year
                )
                db.session.add(series_info)

        db.session.commit()
        print("Series_Info seeded successfully")

        print("Seeding Trailers")

        trailers_data = [
            {"trailer_title": "The Amazing Spider-Man", "video_url": "https://youtu.be/-tnxzJ0SSOw?si=5KIJncsQKKggyzxM"},
            {"trailer_title": "Fast and Furious 6", "video_url": "https://youtu.be/oc_P11PNvRs?si=ObjTbpV4KFohk7NP"},
            {"trailer_title": "Avengers: Infinity War", "video_url": "https://youtu.be/QwievZ1Tx-8?si=bBX8tXlQbI1vWwFs"},
            {"trailer_title": "Avengers: Endgame", "video_url": "https://youtu.be/TcMBFSGVi1c?si=eK_yR1umBENvTsoT"},
            {"trailer_title": "Captain America: The Winter Soldier", "video_url": "https://youtu.be/7SlILk2WMTI?si=gQm1-cLidYe0KjJI"},
            {"trailer_title": "Breaking Bad", "video_url": "https://youtu.be/HhesaQXLuRY?si=8hP-1K61B09Rz2Fj"},
            {"trailer_title": "Game of Thrones", "video_url": "https://youtu.be/KPLWWIOCOOQ?si=7NMoH1c8FXkIv3a0"},
            {"trailer_title": "Stranger Things", "video_url": "https://youtu.be/b9EkMc79ZSU?si=g9FJp_x0xJdlAqwK"},
            {"trailer_title": "The Crown", "video_url": "https://youtu.be/JWtnJjn6ng0?si=c5TQ-dmpCxHyvSWf"},
            {"trailer_title": "The Mandalorian", "video_url": "https://youtu.be/aOC8E8z_ifw?si=Uoah8-GJRrSAMe-5"},
            {"trailer_title": "Friends", "video_url": "https://youtu.be/LTpmw0Ac6Zs?si=1rvjpcii6RDNJUhu"}
    ] 

        for trailer_item in trailers_data:
            movie = Movies.query.filter_by(title=trailer_item['trailer_title']).first()
            if movie:
                trailer = Trailer(trailer_title=trailer_item['trailer_title'], video_url=trailer_item['video_url'], movie_id=movie.id)
                db.session.add(trailer)
            else:
                series = Series.query.filter_by(title=trailer_item['trailer_title']).first()
                if series:
                    # Use series title as the trailer title
                    trailer = Trailer(trailer_title=trailer_item['trailer_title'], video_url=trailer_item['video_url'], series_id=series.id)
                    db.session.add(trailer)

        db.session.commit()
        print("Trailers seeded successfully")

if __name__ == "__main__":
    seed_data()