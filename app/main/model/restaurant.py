from app.main import db
from app.main.model import user
from app.main.model.menu import Menu
from app.main.model.reservation import Reservation

class Restaurant(db.Model):

    """
    Restaurant model for storing restaurant related details
    """

    __tablename__ = 'restaurants'

    id =  db.Column(db.Integer, primary_key=True)
    restaurant_image = db.Column(db.String(255), nullable=True)
    restaurant_thumbnail = db.Column(db.String(255), nullable=True)
    restaurant_thumbnail2 = db.Column(db.String(255), nullable=True)
    restaurant_name = db.Column(db.String(100), nullable=False, unique=True)
    restaurant_type = db.Column(db.String(75), nullable=False)
    location = db.Column(db.String(155), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    opening_day = db.Column(db.String(55))
    closing_day = db.Column(db.String(55))
    opening_time = db.Column(db.String(15), nullable=False)
    closing_time = db.Column(db.String(15), nullable=False)
    no_of_vacancies = db.Column(db.Integer, nullable=False)
    contact_number = db.Column(db.String(11), nullable=False)
    telephone_number = db.Column(db.String(8), nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    restaurant_menu = db.relationship('Menu', backref='menu', lazy='dynamic', cascade="all, delete")
    reservations = db.relationship('Reservation', backref='restaurant', lazy='dynamic', cascade="all, delete")

    def __repr__(self):
        return "<Restaurant '{}'>".format(self.restaurant_name)
    
    def add(self):
        db.session.add(self)
        db.session.commit()