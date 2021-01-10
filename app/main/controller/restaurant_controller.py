from flask import request
from flask_restx import Resource

from app.main.util.dto import RestaurantDto
from app.main.util.custom_dto import RestaurantDtoPublic
from app.main.util.decorator import selective_marshal_with,owner_token_required
from app.main.service.restaurant_service import Rest
from app.main.service.auth_helper import Auth

api = RestaurantDto.api
_restaurant = RestaurantDto.restaurant

@api.route('/')
class RestaurantList(Resource):
  """
  Shows all restaurants
  """
  @api.doc('get_restaurants')
  @selective_marshal_with(RestaurantDtoPublic, name="Restaurants")
  def get(self):
    """
    Get all restaurants
    """
    return Rest.get_all_restaurants()

@api.route('/<int:restaurant_id>')
class Restaurant(Resource):
  """
  Show one restaurant
  """
  @api.doc('get_restaurant')
  @selective_marshal_with(RestaurantDtoPublic, name="Restaurant")
  def get(self, restaurant_id):
    """
    Get one restaurant
    """
    restaurant = Rest.get_a_restaurant(id=restaurant_id)
    if not restaurant:
      api.abort(404, 'Restaurant not found.')
    return restaurant



@api.route('/owner/')
class RestaurantOwner(Resource):
  """
  Restaurant owner operations
  """
  @owner_token_required
  @api.doc('create_restaurant')
  @api.expect(_restaurant, validate=True)
  @api.response(201, 'Restaurant successfully created')
  @api.response(409, 'Restaurant already exists')
  def post(self):
    """
    Create restaurant
    """
    return Rest.add(data=request.json, owner=Auth.get_current_user(request))

  @owner_token_required
  @selective_marshal_with(RestaurantDtoPublic, name="Restaurants")
  def get(self):
    """
    Get all owner's restaurants
    """
    return Rest.get_restaurants(owner=Auth.get_current_user(request))

@api.route('/owner/<int:restaurant_id>')
@api.param('restaurant_id','Restaurant id')
class RestaurantOwnerList(Resource):
  """
  Shows a single restaurant and lets you update and delete an existing restaurant
  """
  @owner_token_required
  @api.expect(_restaurant, validate=True)
  @api.response(200, 'Successfully updated!')
  @api.response(404, 'Restaurant not found')
  def put(self, restaurant_id):
    """
    Update an existing restaurant
    """
    restaurant = Rest.get_a_restaurant(id=restaurant_id)
    if not restaurant:
      api.abort(404, "Restaurant {} not found.".format(restaurant_id))
    return Rest.update(data=request.json, id=restaurant_id)
  
  @owner_token_required
  @api.response(204, "Successfully deleted")
  @api.response(404, "Restaurant not found")
  def delete(self, restaurant_id):
    """
    Delete a restaurant
    """
    restaurant = Rest.get_a_restaurant(id=restaurant_id)
    if not restaurant:
      api.abort(404, "Restaurant {} not found.".format(restaurant_id))
    return Rest.delete(data=request.json, id=restaurant_id)