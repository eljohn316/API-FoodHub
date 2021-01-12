import datetime

from app.main import db
from app.main.model import user

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

class Menu(db.Model):
  """ Menu model for storing menu related details """

  __tablename__ = "menu"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), unique=True)

  items = db.relationship('Item', backref='menu', lazy="joined")

  def __repr__(self):
    return "<Menu '{}'>".format(self.id)

  @staticmethod
  def create(data):
    db.session.add(data)
    db.session.commit()
  
  @staticmethod
  def delete(data):
    db.session.delete(data)
    db.session.commit()

class Item(db.Model):
  """
  Item model for storing menu-item related details
  """
  __tablename__ = "item"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  item_name = db.Column(db.String(100), nullable=False)
  item_availability = db.Column(db.Boolean, default=False)
  price = db.Column(db.String(55), nullable=False)
  image_url = db.Column(db.String(100))

  menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)

  def __repr__(self):
    return "<Item '{}'>".format(self.item_name)