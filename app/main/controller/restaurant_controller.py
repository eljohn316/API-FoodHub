from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from app.main.util.decorator import owner_required, token_required

from ..util.dto import RestaurantDto
from ..service.restaurant_service import create_restaurant, get_all_restaurants

api = RestaurantDto.api
_restaurant = RestaurantDto.restaurant

@api.route('/all')
class RestaurantList(Resource):
    @api.doc('list_of_all_restaurants')
    @owner_required
    @api.marshal_list_with(_restaurant, envelope='Restaurants')
    def get(self):
        return get_all_restaurants()

@api.route('/create')
class AddRestaurant(Resource):
    @api.response(201, "Restaurant created successfully.")
    @owner_required
    @api.doc("Create a restaurant.")
    @api.expect(_restaurant, validate=True)
    def post(self):
        restaurant_data = request.json
        owner = Auth.get_logged_in_user(request)
        owner_id = owner[0]["data"]["user_id"]
        return create_restaurant(data=restaurant_data, owner_id=owner_id)