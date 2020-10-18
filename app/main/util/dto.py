from flask_restx import Namespace, fields

class UserDto:
  api = Namespace('user', description='user related operations')
  create_user = api.model('create_user', {
    'full_name': fields.String(required=True, description='user fullname'),
    'email': fields.String(required=True, description='user email'),
    'password': fields.String(required=True, description='user password'),
    'contact_number': fields.String(required=True, description='user contact number')
  })

  update_user = api.model('update_user', {
    'full_name': fields.String(required=True, description='user fullname'),
    'email': fields.String(required=True, description='user email'),
    'contact_number': fields.String(required=True, description='user contact number')
  })

class AuthDto:
  api = Namespace('auth', description='authentication related operations')
  user_auth = api.model('auth_details', {
    'email': fields.String(required=True, description='email address'),
    'password': fields.String(required=True, description='user password '),
  })