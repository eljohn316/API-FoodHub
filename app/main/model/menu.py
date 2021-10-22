from app.main import db
from app.main.model import restaurant


class Menu(db.Model):
    """
    Menu model for storing menu related details
    """

    id = db.Column(db.Integer, primary_key=True)
    menu_image = db.Column(db.String(255), nullable=True)
    menu_name = db.Column(db.String(100), nullable=False)
    is_available = db.Column(db.String(10), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    def __repr__(self):
        return "<Menu '{}'>".format(self.menu_name)

