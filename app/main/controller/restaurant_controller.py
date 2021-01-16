from flask import request, abort
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
  @api.response(404, "No restaurants found.")
  @selective_marshal_with(RestaurantDtoPublic, name="Restaurants")
  def get(self):
    """
    Get all restaurants
    """
    
    restaurants = Rest.get_all_restaurants()
    if restaurants:
      return restaurants
    abort(404, "No restaurants found.")

@api.route('/<int:restaurant_id>')
class Restaurant(Resource):
  """
  Show one restaurant
  """
  @api.doc('get_restaurant')
  @api.response(404, 'Restaurant not found')
  @selective_marshal_with(RestaurantDtoPublic, name="Restaurant")
  def get(self, restaurant_id):
    """
    Get one restaurant
    """
    restaurant = Rest.get_a_restaurant(restaurant_id=restaurant_id)
    if restaurant:
      return restaurant
    abort(404, "No restaurant found.")
    
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
  @api.response(404, "No restaurants found.")
  @selective_marshal_with(RestaurantDtoPublic, name="Restaurants")
  def get(self):
    """
    Get all owner's restaurants
    """
    restaurants = Rest.get_restaurants(owner=Auth.get_current_user(request))
    if restaurants:
      return restaurants
    abort(404, "No restaurants found.")

@api.route('/owner/<int:restaurant_id>')
@api.response(404, 'Restaurant not found')
@api.param('restaurant_id','Restaurant id')
class RestaurantOwnerList(Resource):
  """
  Shows a single restaurant and lets you update and delete an existing restaurant
  """
  @owner_token_required
  @api.expect(_restaurant, validate=True)
  @api.response(200, 'Successfully updated')
  def put(self, restaurant_id):
    """
    Update an existing restaurant
    """
    restaurant = Rest.get_a_restaurant(restaurant_id=restaurant_id)
    if not restaurant:
      api.abort(404, "Restaurant {} not found.".format(restaurant_id))
    return Rest.update(data=request.json, id=restaurant_id)
  
  @owner_token_required
  @api.response(204, "Successfully deleted")
  def delete(self, restaurant_id):
    """
    Delete a restaurant
    """
    restaurant = Rest.get_a_restaurant(restaurant_id=restaurant_id)
    if not restaurant:
      api.abort(404, "Restaurant {} not found.".format(restaurant_id))
    return Rest.delete(data=request.json, id=restaurant_id)