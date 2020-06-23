from sqlalchemy import Column, String,Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "d6jr987dj82juo"
    database_path = "postgres://{}/{}".format('yzifohghzozjuu:64522481e97787a86418467b993a63047d16e51733c525083ee5eba3eb9c265b@ec2-35-172-73-125.compute-1.amazonaws.com:5432', database_name)

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
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}