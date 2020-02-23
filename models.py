import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

'''
Deploy a flask application to Heroku
'''
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path or 'postgresql://localhost:5432/agency'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()

    migrate = Migrate(app, db)

movie_cast = db.Table('movie_cast',
    db.Column('movie_id', db.Integer, db.ForeignKey('Movie.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('Actor.id'), primary_key=True)
)

'''
Movie
Have title and release year
'''
class Movie(db.Model):  
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    releaseDate = Column(Date)
    actors = db.relationship('Actor', secondary=movie_cast, backref=db.backref('movies', lazy=True))

    def __init__(self, title, releaseDate):
        self.title = title
        self.releaseDate = releaseDate

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'release date': self.releaseDate}

class Actor(db.Model):  
    __tablename__ = 'Actor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'gender': self.gender}
