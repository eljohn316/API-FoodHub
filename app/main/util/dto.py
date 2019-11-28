from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'full_name': fields.String(required=True, description='user full name '),
        'contact_number': fields.String(required=True, description='user contact number'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'user_type': fields.String(required=True, description='user type')
    })
    
class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })