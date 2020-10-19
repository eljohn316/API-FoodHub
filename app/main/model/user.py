import datetime
import jwt

from app.main import db, flask_bcrypt
from app.main.model.blacklist import BlacklistToken
from app.main.model.restaurant import Restaurant
from app.main.config import key

class User(db.Model):
  """ User related details """

  __tablename__ = "user"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  public_id = db.Column(db.String(100), nullable=False, unique=True)
  full_name = db.Column(db.String(155), nullable=False)
  email = db.Column(db.String(50), nullable=False)
  password_hash = db.Column(db.String(100), nullable=False)
  contact_number = db.Column(db.String(15))
  registered_on = db.Column(db.DateTime, nullable=False)
  user_type = db.Column(db.String(20), nullable=False)

  restaurants = db.relationship('Restaurant', backref='owner', lazy=True)

  @property
  def password(self):
    raise AttributeError('password: write-only field')

  @password.setter
  def password(self,password):
    self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
  
  def check_password(self, password):
    return flask_bcrypt.check_password_hash(self.password_hash, password)

  def __repr__(self):
    return "<User '{}'>".format(self.full_name)
  
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
      is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
      if is_blacklisted_token:
        return 'Token blacklisted. Please log in again.'
      else:
        return payload['sub']
    except jwt.ExpiredSignatureError:
      return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
      return 'Invalid token. Please log in again.'