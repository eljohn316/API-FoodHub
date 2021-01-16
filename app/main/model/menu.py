from app.main import db
from app.main.model import restaurant
from app.main.model.item import Item

class Menu(db.Model):
  """ Menu model for storing menu related details """

  __tablename__ = "menu"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
  items = db.relationship('Item', backref='menu', lazy="joined", cascade="all, delete")

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