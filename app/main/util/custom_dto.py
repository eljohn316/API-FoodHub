from flask_restplus import Model, fields

UserDtoPublic = Model('user_public', {
    'email': fields.String(),
    'full_name': fields.String(),
    'contact_number': fields.String(),
    'gender': fields.String()    
})

ReservationDtoPublic = Model('reservation_public', {
    'reservation_code': fields.String(),
    'no_of_persons': fields.String(),
    'date': fields.String(),
    'time': fields.String(),
    'reservation_to': fields.String(),
    'rerservee':fields.String()
})

RestaurantDtoPublic = Model('restaurant_public', {
    'public_id': fields.String(),
    'name': fields.String(),
    'restaurant_type': fields.String(),
    'location': fields.String(),
    'contact_information': fields.String(),
    'owner_id':fields.String()
})