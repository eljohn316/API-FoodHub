from flask import request
from flask_restx import Resource

from app.main.service.restaurant_service import add_restaurant, get_restaurants
from app.main.service.auth_helper import Auth
from app.main.util.dto import RestaurantDto
from app.main.util.custom_dto import RestaurantDtoPublic
from app.main.util.decorator import selective_marshal_with ,owner_token_required

api = RestaurantDto.api
_create_restaurant = RestaurantDto.create_restaurant

@api.route('/')
class RestaurantList(Resource):
  """ Shows all restaurants and lets you POST to add new restaurant. """
  @owner_token_required
  @api.doc('create_restaurant')
  @api.expect(_create_restaurant, validate=True)
  @api.response(201, 'Restaurant successfully created')
  def post(self):
    """ Add restaurant """
    restaurant_data = request.json
    owner_id = Auth.get_current_id(request)
    return add_restaurant(data=restaurant_data, owner_id=owner_id)

  @api.doc('get_restaurants')
  @selective_marshal_with(RestaurantDtoPublic, name="Restaurants")
  def get(self):
    """ Get all restaurants """
    return get_restaurants()

