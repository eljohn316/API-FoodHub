from .. import db

from app.main.model import restaurant
from app.main.model import user

class Reviews(db.Model):

    """ Reviews Model """

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    star_rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    reviewer = db.Column(db.Integer, db.ForeignKey('user.id'))
    reviewed_restaurant = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return "<Reviews '{}'>".format(self.star_rating)
