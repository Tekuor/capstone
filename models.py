import os
from sqlalchemy import Column, String, create_engine, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']

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
Movie
Have title and release date
'''
class Movie(db.Model):  
  __tablename__ = 'Movie'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = db.Column(db.DateTime)
  image_url = Column(String)

  def __init__(self, title, release_date, image_url):
    self.title = title
    self.release_date = release_date
    self.image_url = image_url

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
      'release_date': self.release_date,
      'image_url': self.image_url}

'''
Actor
Have name, age and gender
'''
class Actor(db.Model):  
  __tablename__ = 'Actor'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = Column(String, nullable=False)
  image_url = Column(String)

  def __init__(self, name, age, gender, image_url):
    self.name = name
    self.age = age
    self.gender = gender
    self.image_url = image_url

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
      'gender': self.gender,
      'image_url': self.image_url}

class MovieRoles(db.Model):
    __tablename__ = 'MovieRoles'

    id = Column(Integer, primary_key=True)
    actor_id = Column(db.Integer, db.ForeignKey('Actor.id'), nullable=False)
    movie_id = Column(db.Integer, db.ForeignKey('Movie.id'), nullable=False)
    role = Column(String)

    def __init__(self, actor_id, movie_id, role):
      self.actor_id = actor_id
      self.role = role
      self.movie_id = movie_id

    def insert(self):
      db.session.add(self)
      db.session.commit()