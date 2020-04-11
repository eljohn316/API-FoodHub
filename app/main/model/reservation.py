from app.main import db

from app.main.model import user
from app.main.model import restaurant

class Reservation(db.Model):

    """ Reservation Model """

    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reservation_code = db.Column(db.String(128), nullable=False)
    no_of_persons = db.Column(db.String(12))
    status = db.Column(db.Boolean, default=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
     
    reservee = db.Column(db.Integer, db.ForeignKey('user.id'))
    reservation_to = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return "<Reservation '{}'>".format(self.reservation_code)