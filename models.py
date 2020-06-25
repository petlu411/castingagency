from sqlalchemy import Column, String,Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "db46n25uht9f5b"
    database_path = "postgres://{}/{}".format('llnyamuzpjjkey:8a3b995dda2341142d180473cc5ba164116f42f0ae71c58e785bbd353f284d4b@ec2-50-19-26-235.compute-1.amazonaws.com:5432', database_name)
    
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Actor
Have name, age and gender
'''
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
      'age': str(self.age),
      'gender': self.gender}

'''
Movie
Have title and release date
'''
class Movie(db.Model):  
  __tablename__ = 'Movie'

  id = Column(Integer, primary_key=True)
  title = Column(String)
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