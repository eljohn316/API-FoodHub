import uuid
import datetime

from app.main import db
from app.main.model.user import User

def sign_up_customer(data):
  user = User.query.filter_by(email=data['email']).first()
  if not user:
    new_user = User(
      public_id = str(uuid.uuid4())[:8],
      full_name = data['full_name'],
      email = data['email'],
      password = data['password'],
      contact_number = data['contact_number'],
      registered_on = datetime.datetime.utcnow(),
      user_type = 'Customer'
    )
    save_user(new_user)
    return generate_token(new_user)
  else:
    response_object = {
      'status':'fail',
      'message':'User already exists. Please login.'
    }
    return response_object, 409

def sign_up_owner(data):
  user = User.query.filter_by(email=data['email']).first()
  if not user:
    new_user = User(
      public_id = str(uuid.uuid4())[:8],
      full_name = data['full_name'],
      email = data['email'],
      password = data['password'],
      contact_number = data['contact_number'],
      registered_on = datetime.datetime.utcnow(),
      user_type = 'Owner'
    )
    save_user(new_user)
    return generate_token(new_user)
  else:
    response_object = {
      'status':'fail',
      'message':'User already exists. Please login.'
    }
    return response_object, 409

def update_user(data, public_id):
  current_user = User.query.filter_by(public_id=public_id).first()
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

def get_current_user(id):
  return User.query.filter_by(id=id).first()

def get_owners():
  return User.query.filter_by(user_type='Owner').all()

def get_user(public_id):
  return User.query.filter_by(public_id=public_id).first()

def get_customers():
  return User.query.filter_by(user_type='Customer').all()


def save_user(data):
  db.session.add(data)
  db.session.commit()