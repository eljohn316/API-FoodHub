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

@api.route('/owner/<int:item_id>')
@api.response(404, 'Item not found')
@api.param('item_id', 'Item id')
class ItemList(Resource):
  """
  Get, Update and Delete an existing item.
  """
  @api.marshal_with(_item, envelope="Item")
  def get(self, item_id):
    """
    Get an item
    """
    item = ItemService.get_item(item_id=item_id)
    if not item:
      api.abort(404, "Item {} not found.".format(item_id))
    return item

  
  @api.expect(_item, validate=True)
  @api.response(200, "Successfully updated")
  def put(self, item_id):
    """
    Update an existing item
    """
    data = request.json
    item = ItemService.get_item(item_id=item_id)
    if not item:
      api.abort(404, "Item {} not found".format(item_id))
    return ItemService.update_item(data=data, item_id=item_id)
  
