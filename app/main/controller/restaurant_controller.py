from flask import request, abort
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from app.main.util.decorator import owner_required, token_required

from ..util.dto import RestaurantDto
from ..service.restaurant_service import create_restaurant, update_restaurant, delete_restaurant, get_all_restaurants, get_a_restaurant, get_restaurants_owned

api = RestaurantDto.api
_restaurant = RestaurantDto.restaurant


@api.route('/')
class RestaurantOperations(Resource):
    @api.doc('list_of_restaurants_by_owner')
    @owner_required
    @api.marshal_list_with(_restaurant, envelope='Restaurants')
    def get(self):
        """ Get all restaurants by owner """
        owner = Auth.get_logged_in_user(request)
        owner_id = owner[0]["data"]["user_id"]
        return get_restaurants_owned(owner_id)

    @api.doc("Create a restaurant.")
    @owner_required
    @api.response(201, "Restaurant successfully created.")
    @api.expect(_restaurant, validate=True)
    def post(self):
        """ Create a restaurant """
        restaurant_data = request.json
        owner = Auth.get_logged_in_user(request)
        owner_id = owner[0]["data"]["user_id"]
        return create_restaurant(data=restaurant_data, owner_id=owner_id)

@api.route('/<public_id>')
@api.param('public_id','The restaurant identifier')
class Restaurant(Resource):
    @api.response(200, "Restaurant successfully updated")
    @owner_required
    @api.doc("Update a restaurant.")
    @api.expect(_restaurant, validate=True)
    def put(self, public_id):
        """ Update an existing restaurant """
        data = request.json
        return update_restaurant(data=data, public_id=public_id)

    @api.response(200, "Restaurant successfully deleted")
    @owner_required
    @api.doc("Delete a restaurant")
    def delete(self, public_id):
        """ Delete a restaurant """
        owner = Auth.get_logged_in_user(request)
        owner_id = owner[0]["data"]["user_id"]
        restaurant = get_a_restaurant(public_id)
        restaurant_id = restaurant.id
        print(restaurant_id)
        return delete_restaurant(restaurant_id, owner_id)

    @owner_required
    @api.doc("Get a restaurant by id")
    @api.marshal_list_with(_restaurant, envelope='Restaurants')
    def get(self, public_id):
        """ Get a restaurant """
        return get_a_restaurant(public_id)

@api.route('/all')
class RestaurantList(Resource):
    @api.doc('list_of_all_restaurants')
    @api.marshal_list_with(_restaurant, envelope='Restaurants')
    def get(self):
        """ Get all restaurants """
        return get_all_restaurants()