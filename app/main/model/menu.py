from app.main import db
from app.main.model import restaurant

class Menu(db.Model):
  """ Menu model for storing menu related details """

  __tablename__ = "menu"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  menu_name = db.Column(db.String(50), default='Menu')
  restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), unique=True)  

  def __repr__(self):
    return "<Menu '{}'>".format(self.menu_name)

