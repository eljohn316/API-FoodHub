from flask import request
from flask_restx import Resource

from app.main.service.menu_service import MenuService
from app.main.service.item_service import ItemService
from app.main.util.decorator import owner_token_required
from app.main.util.dto import MenuDto
from app.main.util.custom_dto import MenuDtoPublic

api = MenuDto.api
_menu = MenuDto.menu
_item = MenuDto.item

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
  
@api.route('/<int:menu_id>')
@api.param('menu_id', 'Menu id')
class MenuList(Resource):
  # @owner_token_required
  @api.marshal_with(MenuDtoPublic, envelope='Menu')
  def get(self,menu_id):
    """
    Get restaurant menu
    """
    return MenuService.get(menu_id=menu_id)

@api.route('/item/<int:menu_id>')
@api.param('menu_id', 'Menu id')
class MenuItem(Resource):
  """
  Add item to an existing menu
  """
  @api.response(201, 'Item successfully added')
  @api.response(404, 'Menu does not exists')
  @api.expect(_item, validate=True)
  def post(self, menu_id):
    """
    Add item
    """
    return ItemService.add_item(data=request.json, menu_id=menu_id)