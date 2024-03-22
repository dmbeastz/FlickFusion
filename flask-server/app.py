from flask import Flask
from models import db, Movies, MovieInfo, Series, SeriesInfo, Trailer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db'

# Initialize SQLAlchemy instance
db.init_app(app)

# Create the tables
with app.app_context():
    db.create_all()
