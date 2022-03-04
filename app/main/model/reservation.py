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
    restaurant_owner_id = db.Column(db.Integer)
    time = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    num_of_persons = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10))
    created_on = db.Column(db.DateTime, nullable=False)
    # customer_email = db.Column(db.String(75))
    # customer_contact_number = db.Column(db.String(11))
    accepted_reservations = db.relationship('AcceptedReservation', backref='accepted_reservation', lazy='dynamic', cascade="all, delete")
    declined_reservations = db.relationship('DeclinedReservation', backref='declined_reservation', lazy='dynamic', cascade="all, delete")
    

    def __repr__(self):
        return "<Reservation '{}'>".format(self.id)
    
class AcceptedReservation(db.Model):
    """
    Reservation model for storing accepted reservation details
    """
    __tablename__ = 'accepted_reservations'
    
    id = db.Column(db.Integer, primary_key=True)
    accepted_reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_approved = db.Column(db.DateTime)
    


class DeclinedReservation(db.Model):
    """
    Reservation model for storing declined reservations details
    """
    __tablename__ = 'declined_reservations'

    id = db.Column(db.Integer, primary_key=True)
    declined_reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.Text)