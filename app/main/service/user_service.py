import uuid
import datetime

from app.main import db
from app.main.model.user import User

class UserService:
  
  @staticmethod
  def generate_token(user):
    try:
      auth_token = user.encode_auth_token(user.id)
      response_object = {
        'status':'success',
        'message':'Successfully registered.',
        'Authorization': auth_token.decode()
      }
      return response_object, 201
    except Exception as e:
      response_object = {
        'status':'fail',
        'message':'Some error occured. Please try again.'
      }
      return response_object, 401

  @staticmethod
  def sign_up(data):
    user = User.find_by_email(email=data['email'])
    if not user:
      new_user = User(
        public_id = str(uuid.uuid4())[:8],
        full_name = data['full_name'],
        email = data['email'],
        password = data['password'],
        contact_number = data['contact_number'],
        registered_on = datetime.datetime.utcnow(),
        user_type = str(data['user_type']).capitalize()
      )
      User.add(new_user)
      return UserService.generate_token(new_user)
    else:
      response_object = {
        'status':'fail',
        'message':'User already exists. Please login.'
      }
      return response_object, 409

  @staticmethod
  def update(data, id):
    current_user = User.find_by_id(id=id)
    if not current_user:
      response_object = {
        'status':'fail',
        'message':'User not found.'
      }
      return response_object, 404
    else:
      current_user.full_name = data['full_name'],
      current_user.email = data['email'],
      current_user.contact_number = data['contact_number']
      db.session.commit()
      response_object = {
        'status':'success',
        'message':'Successfully updated'
      }
      return response_object, 200

  @staticmethod
  def get_user(id):
    return User.find_by_id(id=id)

  @staticmethod
  def get_owners():
    return User.query.filter_by(user_type='Owner').all()

  @staticmethod
  def get_customers():
    return User.query.filter_by(user_type='Customer').all()

  




