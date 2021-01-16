from flask_restx import Model, fields

UserDtoPublic = Model('user', {
  'id' : fields.String(),
  'full_name': fields.String(),
  'contact_number': fields.String(),
  'account_details': {
    'public_id':fields.String(),
    'email': fields.String(),
    'registered_on': fields.DateTime(dt_format='rfc822'),
  }
})

RestaurantDtoPublic = Model('restaurant', {
  'restaurant_id' : fields.String(),
  'public_id' : fields.String(),
  'restaurant_name' : fields.String(),
  'restaurant_details' : {
    'restaurant_type' : fields.String(),
    'business_hours' : fields.String(),
    'location' : fields.String(),
    'contact_number' : fields.String(),
    'telephone_number' : fields.String(),
    'date_created' : fields.DateTime(dt_format='rfc822'),
    'owner': {
      'owner_id' : fields.String(),
      'profile_image' : fields.String(),
      'full_name' : fields.String(),
      'email' : fields.String(),
      'owner_contact_number' : fields.String(),
      'registered_on': fields.String(),
      'user_type': fields.String(),
    }
  }
})

MenuDtoPublic = Model('menu', {
  'id' : fields.Integer(),
  'item_name' : fields.String(),
  'is_sold_out' : fields.Boolean(),
  'price' : fields.Float(),
  'image_url' : fields.String()
})