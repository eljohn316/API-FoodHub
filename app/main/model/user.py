import datetime
import jwt

from app.main import db, flask_bcrypt
from app.main.config import key
from app.main.model import restaurant
from app.main.model.blacklist import BlackListToken
from app.main.model.restaurant import Restaurant
from app.main.model.reservation import Reservation

class User(db.Model):
    """
    User model for storing user related operations
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(255), nullable=True)
    profile_image2 = db.Column(db.String(255), nullable=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(100))
    contact_number = db.Column(db.String(11), nullable=False)
    user_role = db.Column(db.String(20), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)

    restaurants = db.relationship('Restaurant', backref='owner', lazy='dynamic', cascade="all, delete")
    reservations = db.relationship('Reservation', backref='customer', lazy='dynamic', cascade="all, delete")

    @property
    def password(self):
        raise AttributeError('password: write-only field')
    
    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def add(self, data):
        db.session.add(data)
        db.session.commit()
    
    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    @staticmethod  
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlackListToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.first_name)
