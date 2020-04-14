from flask_restplus import Namespace, fields 

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'full_name': fields.String(required=True, description='user full name '),
        'contact_number': fields.String(required=True, description='user contact number'),
        'gender': fields.String(required=True, description='user gender'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'user_type': fields.String(required=True, description='user type')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username_or_email': fields.String(required=True, description='user username or email address'),
        'password': fields.String(required=True, description='user password '),
    })


class RestaurantDto:
    api = Namespace('restaurant', description='restaurant related operations')
    restaurant = api.model('restaurant', {
        'name': fields.String(required=True, description='restaurant name'),
        'restaurant_type': fields.String(required=True, description='restaurant type'),
        'location': fields.String(required=True, description='restaurant location'),
        'contact_information': fields.String(required=True, description='restaurant contact information')
    })

class MenuDto:
    api = Namespace('menu', description='menu related operations')
    menu = api.model('menu',{
        'menu_pic': fields.String(required=True, description='menu profile picture'),
        'name': fields.String(required=True, description='menu name'),
        'category': fields.String(required=True, description='menu category'),
        'price': fields.String(required=True, description='menu price'),
        'restaurant_id': fields.String(required=True, description='restaurant id')
    })

class ReservationDto:
    api = Namespace('reservation', description='reservation related operations')
    reservation = api.model('reservation', {
        'no_of_persons': fields.String(required=True, description='reservation number of persons'),
        'date': fields.String(required=True, description='reservation date'),
        'time': fields.String(required=True, description='reservation time'),
        'reservation_to': fields.String(required=True, description='reservation restaurant')
    })