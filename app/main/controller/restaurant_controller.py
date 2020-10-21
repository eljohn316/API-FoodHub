from flask import request
from flask_restx import Resource

from app.main.service.restaurant_service import add_restaurant, get_restaurants, get_my_restaurants, get_a_restaurant, update_restaurant
from app.main.service.auth_helper import Auth
from app.main.util.dto import RestaurantDto
from app.main.util.custom_dto import RestaurantDtoPublic
from app.main.util.decorator import selective_marshal_with ,owner_token_required

api = RestaurantDto.api
_restaurant = RestaurantDto.restaurant

@api.route('/')
class RestaurantList(Resource):
  """ Shows all restaurants and lets you POST to add new restaurant. """
  @owner_token_required
  @api.doc('create_restaurant')
  @api.expect(_restaurant, validate=True)
  @api.response(201, 'Restaurant successfully created')
  def post(self):
    """ Add restaurant """
    restaurant_data = request.json
    return add_restaurant(data=restaurant_data, owner_id=Auth.get_current_id(request))

  @owner_token_required
  @selective_marshal_with(RestaurantDtoPublic, name="Restaurants")
  def get(self):
    """ Get currently logged in owner's restaurant """
    return get_my_restaurants(owner_id=Auth.get_current_id(request))

@api.route('/<public_id>')
@api.param('public_id','Restaurant public id')
class Restaurant(Resource):
  """ Shows a single restaurant and lets you update and delete an existing restaurant. """
  @owner_token_required
  @api.expect(_restaurant, validate=True)
  @api.response(200, 'Successfully Updated!')
  @api.response(404, 'Restaurant not found')
  def put(self, public_id):
    """ Update an existing restaurant """
    data = request.json
    restaurant = get_a_restaurant(public_id=public_id)
    if restaurant and Auth.get_current_id(request) == restaurant.owner_id:
      print('pasok')
      return update_restaurant(data=data, public_id=public_id)
    else:
      print('sad lyf')
      api.abort(404, "Restaurant {} not found.".format(public_id))

@api.doc('get_restaurants')
@selective_marshal_with(RestaurantDtoPublic, name="Restaurants")
def get(self):
  """ Get all restaurants """
  return get_restaurants()



