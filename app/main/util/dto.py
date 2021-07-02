from flask_restx import Model, Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id' : fields.String(description='user id'),
        'profile_image' : fields.String(description='user image'),
        'email' : fields.String(description='user email'),
        'first_name' : fields.String(description='user first name'),
        'last_name' : fields.String(description='user last name'),
        'contact_number' : fields.String(description='user contact number'),
        'user_role' : fields.String(description='user role'),
        'date_joined' : fields.String(description='user join date')
    })

    user_create = api.model('create_user', {
        'email' : fields.String(required=True, description='user email'),
        'first_name' : fields.String(required=True, description='user first name'),
        'last_name' : fields.String(required=True, description='user last name'),
        'password' : fields.String(required=True, description='user password'),
        'contact_number' : fields.String(required=True, description='user contact number'),
        'user_role' : fields.String(required=True, description='user role')
    })

    user_update = api.model('update_user', {
        'email' : fields.String(description='user email'),
        'first_name' : fields.String(description='user first name'),
        'last_name' : fields.String(description='user last name'),
        'contact_number' : fields.String(description='user contact number')
    })

    set_profile = api.model('update_user', {
        'profile_image' : fields.String(description='user profile image')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='user email '),
        'password': fields.String(required=True, description='user password '),
    })

class RestaurantDto:
    api = Namespace('restaurant', description='restaurant related operations')
    create_restaurant = api.model('create_restaurant', {
        'restaurant_image' : fields.String(required=True, description='restaurant image'),
        'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'), 
        'restaurant_name' : fields.String(required=True, description='restaurant name'),
        'restaurant_type' : fields.String(required=True, description='restaurant type'),
        'location' : fields.String(required=True, description='restaurant location'),
        'opening_day' : fields.String(required=True, description='opening day'),
        'closing_day' : fields.String(required=True, description='closing day'),
        'opening_time' : fields.String(required=True, description='opening time'),
        'closing_time' : fields.String(required=True, description='closing time'),
        'no_of_vacancies' : fields.Integer(required=True, description='number of vacancies'),
        'contact_number' : fields.String(required=True, description='contact number'),
        'telephone_number' : fields.String(required=True, description='telephone number'),
        'owner_id' : fields.Integer(required=True, description='owner id')
    })

    update_restaurant = api.model('update_restaurant', {
        'restaurant_name' : fields.String(required=True, description='restaurant name'),
        'restaurant_type' : fields.String(required=True, description='restaurant type'),
        'location' : fields.String(required=True, description='restaurant location'),
        'opening_day' : fields.String(required=True, description='opening day'),
        'closing_day' : fields.String(required=True, description='closing day'),
        'opening_time' : fields.String(required=True, description='opening time'),
        'closing_time' : fields.String(required=True, description='closing time'),
        'no_of_vacancies' : fields.Integer(required=True, description='number of vacancies'),
        'contact_number' : fields.String(required=True, description='contact number'),
        'telephone_number' : fields.String(required=True, description='telephone number')
    })

    get_restaurant = api.model('get_restaurants', {
        'restaurant_id' : fields.String(required=True, description='restaurant id'),
        'restaurant_image' : fields.String(required=True, description='restaurant image'),
        'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'), 
        'restaurant_name' : fields.String(required=True, description='restaurant name'),
        'restaurant_type' : fields.String(required=True, description='restaurant type'),
        'location' : fields.String(required=True, description='restaurant location'),
        'date_created' : fields.String(required=True, description='date created'),
        'opening_day' : fields.String(required=True, description='opening day'),
        'closing_day' : fields.String(required=True, description='closing day'),
        'opening_time' : fields.String(required=True, description='opening time'),
        'closing_time' : fields.String(required=True, description='closing time'),
        'no_of_vacancies' : fields.Integer(required=True, description='number of vacancies'),
        'contact_number' : fields.String(required=True, description='contact number'),
        'telephone_number' : fields.String(required=True, description='telephone number'),
        'owner_id' : fields.Integer(required=True, description='owner id')
    })

class RestaurantPublicDto:
    restaurant = Model('restaurant', {
        'restaurant_id' : fields.String(required=True, description='restaurant id'),
        'restaurant_image' : fields.String(required=True, description='restaurant image'),
        'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'),
        'restaurant_name' : fields.String(required=True, description='restaurant name'),
        'restaurant_type' : fields.String(required=True, description='restaurant type'),
        'location' : fields.String(required=True, description='restaurant location'),
        'date_created' : fields.String(required=True, description='date created'),
        'opening_day' : fields.String(required=True, description='opening day'),
        'closing_day' : fields.String(required=True, description='closing day'),
        'opening_time' : fields.String(required=True, description='opening time'),
        'closing_time' : fields.String(required=True, description='closing time'),
        'no_of_vacancies' : fields.Integer(required=True, description='number of vacancies'),
        'contact_number' : fields.String(required=True, description='contact number'),
        'telephone_number' : fields.String(required=True, description='telephone number'),
        'owner_details' : {
            'owner_id' : fields.Integer(description='user id'),
            'profile_image' : fields.String(description='user profile_image'),
            'email' : fields.String(description='user email'),
            'first_name' : fields.String(description='user first name'),
            'last_name' : fields.String(description='user last name'),
            'contact_number' : fields.String(description='user contact number')
        }
    })