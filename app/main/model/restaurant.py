import datetime

from app.main import db
from app.main.model import user
from app.main.model.menu import Menu

class Restaurant(db.Model):
  """ Restaurant model for storing restaurant related details """

  __tablename__ = "restaurant"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  public_id = db.Column(db.String(20), nullable=False, unique=True)
  restaurant_image = db.Column(db.String(155), nullable=True)
  restaurant_name = db.Column(db.String(100), nullable=False, unique=True)
  restaurant_type = db.Column(db.String(100), nullable=False)
  business_hours = db.Column(db.String(100), nullable=False)
  location = db.Column(db.String(155), nullable=False)
  contact_number = db.Column(db.String(20), nullable=False)
  telephone_number = db.Column(db.String(20), nullable=False)
  date_created = db.Column(db.DateTime, nullable=False)

  owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  menu = db.relationship('Menu', backref='restaurant', uselist=False)

  def __repr__(self):
    return "<User '{}'>".format(self.restaurant_name)
  
  @staticmethod
  def add(data):
    db.session.add(data)
    db.session.commit()

  @staticmethod
  def delete(data):
    db.session.delete(data)
    db.session.commit()