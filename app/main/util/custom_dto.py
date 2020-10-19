from flask_restx import Model, fields

UserDtoPublic = Model('user', {
  'full_name': fields.String(),
  'contact_number': fields.String(),
  'account': {
    'public_id':fields.String(),
    'email': fields.String(),
    'registered_on': fields.DateTime(dt_format='rfc822'),
  }
})

RestaurantDtoPublic = Model('restaurant', {
  'public_id' : fields.String(),
  'restaurant_name' : fields.String(),
  'restaurant_type' : fields.String(),
  'business_hours' : fields.String(),
  'location' : fields.String(),
  'contact_number' : fields.String(),
  'telephone_number' : fields.String(),
  'date_created' : fields.DateTime(dt_format='rfc822'),
  'owner': {
    'owner_id' : fields.String()
  }
})
