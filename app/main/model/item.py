from app.main import db
from app.main.model import menu

class Item(db.Model):
  """
  Item model for storing menu-item related details
  """
  __tablename__ = "item"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  item_name = db.Column(db.String(100), nullable=False)
  price = db.Column(db.Float, nullable=False)
  image_url = db.Column(db.String(100))

  menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)

  def __repr__(self):
    return "<Item '{}'>".format(self.item_name)