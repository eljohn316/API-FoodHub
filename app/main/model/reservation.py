from app.main import db
from app.main.model import restaurant
from app.main.model import user

class Reservation(db.Model):
    """
    Reservation model for storing reservation related details
    """
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    num_of_persons = db.Column(db.Integer, nullable=False)
    is_accepted = db.Column(db.String(10), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    customer_email = db.Column(db.String(75))
    customer_contact_number = db.Column(db.String(11))

    def __repr__(self):
        return "<Reservation '{}'>".format(self.id)