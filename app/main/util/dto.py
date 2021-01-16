from flask_restx import Namespace, fields

class OwnerDto:
  api = Namespace('owner', description='owner related operations')
  create_owner = api.model('create_owner', {
    'full_name': fields.String(required=True, description='owner fullname'),
    'email': fields.String(required=True, description='owner email'),
    'password': fields.String(required=True, description='owner password'),
    'contact_number': fields.String(required=True, description='owner contact number'),
    'user_type': fields.String(readonly=True, default="Owner", description='owner type')
  })

  update_owner = api.model('update_owner', {
    'full_name': fields.String(required=True, description='owner fullname'),
    'email': fields.String(required=True, description='owner email'),
    'contact_number': fields.String(required=True, description='owner contact number')
  })

class CustomerDto:
  api = Namespace('customer', description='customer related operations')
  create_customer = api.model('create_customer', {
    'full_name': fields.String(required=True, description='customer fullname'),
    'email': fields.String(required=True, description='customer email'),
    'password': fields.String(required=True, description='customer password'),
    'contact_number': fields.String(required=True, description='customer contact number'),
    'user_type': fields.String(readonly=True, description='customer type')
  })

  update_customer = api.model('update_customer', {
    'full_name': fields.String(required=True, description='customer fullname'),
    'email': fields.String(required=True, description='customer email'),
    'contact_number': fields.String(required=True, description='customer contact number')
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

class ItemDto:
  api = Namespace('item', description="item related operations")
  item = api.model('item', {
    'id' : fields.Integer(readonly=True, description='item id'),
    'item_name' : fields.String(required=True, description='item name'), 
    'price' : fields.Float(required=True, min=0, description='item price'),
    'image_url' : fields.String(readonly=True, description="item image")
  })