from flask_restx import Model, Namespace, fields
from flask_cors import cross_origin

class UserDto:
    api = Namespace('user', description='user related operations', decorators=[cross_origin()])
    user = api.model('user', {
        'id' : fields.String(description='user id'),
        'profile_image' : fields.String(description='user image'),
        'profile_image2' : fields.String(description='user secondary profile image'),
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
        'profile_image' : fields.String(description='user profile image'),
        'profile_image2' : fields.String(description='user profile image 2')
    })

    update_password = api.model('update_password', {
        'new_password' : fields.String(description='user new password')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations', decorators=[cross_origin()])
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='user email '),
        'password': fields.String(required=True, description='user password '),
    })

class RestaurantDto:
    api = Namespace('restaurant', description='restaurant related operations', decorators=[cross_origin()])
    create_restaurant = api.model('create_restaurant', {
        # 'restaurant_image' : fields.String(required=True, description='restaurant image'),
        # 'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'),
        # 'restaurant_thumbnail2' : fields.String(required=True, description='restaurant image thumbnail'),
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

    set_image = api.model('set_restaurant_image', {
        'restaurant_image' : fields.String(required=True, description='restaurant image'),
        'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'),
        'restaurant_thumbnail2' : fields.String(required=True, description='restaurant image thumbnail')
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

    menu = api.model('menu', {
        'menu_id' : fields.Integer(),
        'menu_image' : fields.String(),
        'menu_name' : fields.String(),
        'is_available' : fields.Boolean(),
        'price' : fields.Float()
    })

    user = api.model('user', {
        'owner_id' : fields.String(description='user id'),
        'profile_image' : fields.String(description='user image'),
        'profile_image2' : fields.String(description='user secondary profile image'),
        'email' : fields.String(description='user email'),
        'first_name' : fields.String(description='user first name'),
        'last_name' : fields.String(description='user last name'),
        'owner_contact_number' : fields.String(description='user contact number'),
        'date_joined' : fields.String(description='user join date')
    })
    

    get_restaurant = api.model('get_restaurants', {
        'restaurant_id' : fields.Integer(required=True, description='restaurant id'),
        'restaurant_image' : fields.String(required=True, description='restaurant image'),
        'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'),
        'restaurant_thumbnail2' : fields.String(required=True, description='restaurant image thumbnail'), 
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
        'owner_id': fields.Integer(required=True, description='telephone number')
    })

    get_single_restaurant = api.model('get_restaurants', {
        'restaurant_id' : fields.Integer(required=True, description='restaurant id'),
        'restaurant_image' : fields.String(required=True, description='restaurant image'),
        'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'),
        'restaurant_thumbnail2' : fields.String(required=True, description='restaurant image thumbnail'), 
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
        'restaurant_menu' : fields.List(fields.Nested(menu)),
        'owner_details' : fields.Nested(user)
    })

    get_restaurant_menu = api.model('get_restaurants', {
        'restaurant_id' : fields.String(required=True, description='restaurant id'),
        'restaurant_image' : fields.String(required=True, description='restaurant image'),
        'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'),
        'restaurant_thumbnail2' : fields.String(required=True, description='restaurant image thumbnail'), 
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
        'restaurant_menu' : fields.List(fields.Nested(menu))
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

class MenuDto:
    api = Namespace('menu', description='menu related operations', decorators=[cross_origin()])
    add_menu = api.model('create_menu', {
        'menu_image' : fields.String(required=False, description='menu image'),
        'menu_name' : fields.String(required=True, description='menu name'),
        'is_available' : fields.String(required=True, description='menu availability'),
        'price' : fields.String(required=True, description='menu price'),
        'restaurant_id' : fields.Integer(required=True, description='restaurant id')
    })

    update_menu = api.model('update_menu', {
        'menu_name' : fields.String(required=True, description='menu name'),
        'is_available' : fields.String(required=True, description='menu availability'),
        'price' : fields.String(required=True, description='menu price')
    })

    get_menu = api.model('get_menu', {
        'id' : fields.Integer(required=True, description='menu id'),
        'menu_image' : fields.String(required=False, description='menu image'),
        'menu_name' : fields.String(required=True, description='menu name'),
        'is_available' : fields.String(required=True, description='menu availability'),
        'price' : fields.String(required=True, description='menu price'),
        'restaurant_id' : fields.Integer(required=True, description='restaurant id')
    })

class ReservationDto:
    api = Namespace('reservation', description='reservation related details', decorators=[cross_origin()])
    create_reservation = api.model('create_reservation', {
        'restaurant_id' : fields.Integer(required=True, description='restaurant id'),
        'restaurant_owner_id': fields.Integer(required=True, description='restaurant owner id'),
        'time' : fields.String(required=True, description='reservation time'),
        'date' : fields.String(required=True, description='reservation date'),
        'num_of_persons' : fields.Integer(required=True, description='number of reservee')
    })

    update_reservation = api.model('update_reservation', {
        'time' : fields.String(required=True, description='reservation time'),
        'date' : fields.String(required=True, description='reservation date'),
        'num_of_persons' : fields.Integer(required=True, description='number of reservee')
    })

    get_reservation = api.model('get_reservation', {
        'id' : fields.Integer(required=True, description='reservation id'),
        'restaurant_id' : fields.Integer(required=True, description='restaurant id'),
        'customer_id' : fields.Integer(required=True, description='customer id'),
        'time' : fields.String(required=True, description='reservation time'),
        'date' : fields.String(required=True, description='reservation date'),
        'num_of_persons' : fields.Integer(required=True, description='number of reservee'),
        'status' : fields.String(required=True, description='reservation status'),
        'created_on' : fields.String(description='reservation date created')
    })

    restaurant = api.model('restaurant', {
        'restaurant_id' : fields.String(required=True, description='restaurant id'),
        'restaurant_image' : fields.String(required=True, description='restaurant image'),
        'restaurant_thumbnail' : fields.String(required=True, description='restaurant image thumbnail'),
        'restaurant_thumbnail2' : fields.String(required=True, description='restaurant image thumbnail'), 
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
        'telephone_number' : fields.String(required=True, description='telephone number')
    })
        

    get_customer_reservation = api.model('get_reservation', {
        'id' : fields.Integer(required=True, description='reservation id'),
        'customer_id' : fields.Integer(required=True, description='customer id'),
        'time' : fields.String(required=True, description='reservation time'),
        'date' : fields.String(required=True, description='reservation date'),
        'num_of_persons' : fields.Integer(required=True, description='number of reservee'),
        'status' : fields.String(required=True, description='reservation status'),
        'created_on' : fields.String(description='reservation date created'),
        'restaurant' : fields.Nested(restaurant)
    })

    decline_reservation = api.model('decline_reservation', {
        'message' : fields.String(description='owner message')
    })

    user = api.model('user', {
        'customer_id' : fields.String(description='user id'),
        'profile_image' : fields.String(description='user image'),
        'profile_image2' : fields.String(description='user secondary profile image'),
        'email' : fields.String(description='user email'),
        'first_name' : fields.String(description='user first name'),
        'last_name' : fields.String(description='user last name'),
        'contact_number' : fields.String(description='user contact number')
    })

    reservation_bookings = api.model('restaurant_bookings', {
        'reservation_id' : fields.Integer(description='reservation id'),
        'time' : fields.String(required=True, description='reservation time'),
        'date' : fields.String(required=True, description='reservation date'),
        'num_of_persons' : fields.Integer(required=True, description='number of reservee'),
        'status' : fields.String(required=True, description='reservation status'),
        'created_on' : fields.String(description='reservation date created'),
        'customer_details' : fields.Nested(user),
        'restaurant_details' : fields.Nested(restaurant)
    })
    