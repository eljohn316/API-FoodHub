from flask_restx import Namespace, fields

class UserDto:
  api = Namespace('user', description='user related operations')
  create_user = api.model('create_user', {
    'full_name': fields.String(required=True, description='user fullname'),
    'email': fields.String(required=True, description='user email'),
    'password': fields.String(required=True, description='user password'),
    'contact_number': fields.String(required=True, description='user contact number'),
    'user_type': fields.String(required=True, description='user type')
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

class RestaurantDto:
  api = Namespace('restaurant', description='restaurant related operations')
  restaurant = api.model('restaurant', {
    'restaurant_name' : fields.String(required=True, description='restaurant name'),
    'restaurant_type' : fields.String(required=True, description='restaurant type'),
    'business_hours' : fields.String(required=True, description='restaurant business hours'),
    'location' : fields.String(required=True, description='restaurant location'),
    'contact_number' : fields.String(required=True, description='restaurant contact number'),
    'telephone_number' : fields.String(required=True, description='restaurant telephone number')
  })

class MenuDto:
  api = Namespace('menu', description='menu related operations')
  menu = api.model('menu', {
    'restaurant_id' : fields.Integer(required=True, description='restaurant id')

  })