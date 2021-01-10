from flask import request
from flask_restx import Resource

from app.main.service.menu_service import MenuService
from app.main.util.decorator import owner_token_required
from app.main.util.dto import MenuDto

api = MenuDto.api
_menu = MenuDto.menu

@api.route('/<int:restaurant_id>')
@api.param('restaurant_id', 'Restaurant id')
class Menu(Resource):
  """
  Create a menu for a restaurant
  """
  # @owner_token_required
  @api.response(201, 'Menu successfully created')
  @api.response(404, 'Restaurant does not exists')
  @api.expect(_menu, validate=True)
  def post(self, restaurant_id):
    """
    Create a restaurant menu
    """
    return MenuService.create(data=request.json, restaurant_id=restaurant_id)
  # @owner_token_required
  @api.marshal_with(_menu, envelope='Restaurant Menu')
  def get(self,restaurant_id):
    """
    Get restaurant menu
    """
    return MenuService.get(id=restaurant_id)
