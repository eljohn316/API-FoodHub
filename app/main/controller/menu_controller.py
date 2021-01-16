from flask import request
from flask_restx import Resource

from app.main.service.menu_service import MenuService
from app.main.util.dto import MenuDto
from app.main.util.decorator import owner_token_required, selective_marshal_with
from app.main.util.custom_dto import MenuDtoPublic

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
  def post(self, restaurant_id):
    """
    Create a restaurant menu
    """
    return MenuService.create(data=request.json, restaurant_id=restaurant_id)
  
@api.route('/<int:menu_id>')
@api.param('menu_id', 'Menu id')
class MenuList(Resource):
  # @owner_token_required
  @selective_marshal_with(MenuDtoPublic, name="Menu")
  def get(self,menu_id):
    """
    Get restaurant menu
    """
    menu = MenuService.get_menu(menu_id=menu_id)
    if not menu:
      abort(404, "Menu not found")
    return menu