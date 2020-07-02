from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ.get('DATABASE_URL')
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    '''
    setup_db(app)
        binds a flask application and a SQLAlchemy service
    '''
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Actor(db.Model):
    '''
    Actor
    Have name, age and gender
    '''
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
          'age': str(self.age),
          'gender': self.gender}


class Movie(db.Model):
    '''
    Movie
    Have title and release date
    '''
    __tablename__ = 'Movie'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    releasedate = Column(String)

    def __init__(self, title, releasedate):
        self.title = title
        self.releasedate = releasedate

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
          'releasedate': self.releasedate}
