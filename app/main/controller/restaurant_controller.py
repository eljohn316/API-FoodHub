from flask import request
from flask_restx import Resource

from app.main.util.dto import RestaurantDto, RestaurantPublicDto
from app.main.service.restaurant_service import RestaurantService as restaurant
from app.main.util.decorator import custom_marshal_with, owner_token_required

api = RestaurantDto.api

_restaurant = RestaurantPublicDto.restaurant
_create_restaurant = RestaurantDto.create_restaurant
_update_restaurant = RestaurantDto.update_restaurant
_get_restaurant = RestaurantDto.get_restaurant

@api.route('/')
class RestaurantList(Resource):
    @owner_token_required
    @api.doc('list_of_restaurants')
    @custom_marshal_with(_restaurant, name='Restaurants')
    def get(self):
        """ Get all restaurants """
        return restaurant.get_restaurants()
    
    @owner_token_required
    @api.response('Restaurant successfully added', 201)
    @api.doc('create_restaurant')
    @api.expect(_create_restaurant, validate=True)
    def post(self):
        """ Create a new restaurant """
        return restaurant.create_restaurant(data=request.json)

@api.route('/<int:id>')
class Restaurant(Resource):
    @owner_token_required
    @api.doc('get_a_restaurant')
    @api.response(404, 'Restaurant not found')
    @custom_marshal_with(_restaurant, name='Restaurant')
    def get(self, id):
        """ Get a single restaurant """
        result = restaurant.get_restaurant(restaurant_id=id)
        if not result:
            api.abort(404, 'User not found')
        return result

    @owner_token_required
    @api.doc('update_a_restaurant')
    @api.response(200, 'Restaurant successfully updated')
    @api.response(404, 'Restaurant not found')
    @api.expect(_update_restaurant, validate=True)
    def put(self, id):
        """ Update an existing restaurant """
        return restaurant.update_restaurant(data=request.json, restaurant_id=id)
    
    @owner_token_required
    @api.doc('delete_a_restaurant')
    @api.response(200, 'Restaurant successfully deleted')
    @api.response(404, 'Restaurant not found')
    def delete(self, id):
        """ Delete an existing restaurant """
        return restaurant.delete_restaurant(restaurant_id=id)

@api.route('/explore')
class RestaurantPublic(Resource):
    @api.doc('explore_restaurants')
    @custom_marshal_with(_get_restaurant, name='Restaurants')
    def get(self):
        """ Explore restaurants """
        return restaurant.get_all_restaurants()