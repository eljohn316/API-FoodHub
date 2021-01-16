from flask import request
from flask_restx import Resource

from app.main.service.item_service import ItemService
from app.main.util.decorator import owner_token_required
from app.main.util.dto import ItemDto

api = ItemDto.api
_item = ItemDto.item

@api.route('/<int:menu_id>')
@api.param('menu_id', 'Menu id')
class Item(Resource):
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

@api.route('/<int:item_id>')
@api.param('item_id', 'Item id')
class ItemList(Resource):
  """
  Update and delete an item
  """
  @api.response(200, 'Item succesfully updated')
  # @api.expect(_item, validate=True)
  def put(self, item_id):
    """
    Update an existing item.
    """
    item = ItemService.get_item(item_id=item_id)
    if not item:
      api.abort("Item {} not found.".format(item_id))
    return ItemService.update_item(data=request.json, item_id=item_id)

