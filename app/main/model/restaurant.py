from .. import db
import datetime
from app.main.model import user
from app.main.model import menu
from app.main.model import reservation

class Restaurant(db.Model):

    """ Restaurant Model"""

    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(155), nullable=False, unique=True)
    restaurant_type = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    contact_information = db.Column(db.String(255), unique=True)
    
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    menu = db.relationship('Menu', backref='restaurant_menu')
    reservation = db.relationship('Reservation', backref='reservation')

    def __repr__(self):
        return "<Restaurant '{}'>".format(self.name)




