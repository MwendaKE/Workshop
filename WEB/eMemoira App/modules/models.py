from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Memoir(db.Model):
    __tablename__ = "memoirs"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(200))
    audios = db.relationship("Audio", backref="memoir", lazy=True)
    pictures = db.relationship("Picture", backref="memoir", lazy=True)
    videos = db.relationship("Video", backref="memoir", lazy=True)
    
    date_created = db.Column(db.DateTime, default=datetime.now)
    date_of_reference = db.Column(db.DateTime)
      
    def __init__(self, title, body, date_of_reference):
      self.title = title
      self.body = body
      self.date_of_reference = date_of_reference
      self.description = (body[:195] + "...") if len(body) > 100 else body
      
      
class Audio(db.Model):
    __tablename__ = "audios"
    id = db.Column(db.Integer, primary_key=True)
    filepath = db.Column(db.String(250), nullable=False)
    memoir_id = db.Column(db.Integer, db.ForeignKey("memoirs.id"), nullable=False)
    
    
class Picture(db.Model):
    __tablename__ = "pictures"
    id = db.Column(db.Integer, primary_key=True)
    filepath = db.Column(db.String(250), nullable=False)
    memoir_id = db.Column(db.Integer, db.ForeignKey("memoirs.id"), nullable=False)
    
    
class Video(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer, primary_key=True)
    filepath = db.Column(db.String(250), nullable=False)
    memoir_id = db.Column(db.Integer, db.ForeignKey("memoirs.id"), nullable=False)
    