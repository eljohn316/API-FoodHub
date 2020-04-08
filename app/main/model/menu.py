from .. import db

from app.main.model import restaurant

class Menu(db.Model):
    
    """ Menu Model """

    __tablename__ = "menu"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_pic = db.Column(db.String(100), nullable=False, default="default_menu_pic.jpg")
    name = db.Column(db.String(255), nullable=False, unique=True)
    category = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return "<Menu '{}'>".format(self.name)