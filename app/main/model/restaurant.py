import datetime

from app.main import db
from app.main.model import user

class Restaurant(db.Model):
  """ Restaurant model for storing restaurant related details """

  __tablename__ = "restaurant"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  public_id = db.Column(db.String(20), nullable=False, unique=True)
  restaurant_name = db.Column(db.String(100), nullable=False, unique=True)
  restaurant_type = db.Column(db.String(100), nullable=False)
  business_hours = db.Column(db.String(100), nullable=False)
  location = db.Column(db.String(155), nullable=False)
  contact_number = db.Column(db.String(20), nullable=False)
  telephone_number = db.Column(db.String(20), nullable=False)
  date_created = db.Column(db.DateTime, nullable=False)

  owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return "<User '{}'>".format(self.restaurant_name)