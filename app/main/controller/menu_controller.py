from flask import request
from flask_restx import Resource

from app.main.service.menu_service import MenuService
from app.main.util.decorator import owner_token_required
from app.main.util.dto import MenuDto

api = MenuDto.api
_menu = MenuDto.menu

@api.route('/<public_id>')
@api.param('public_id', 'Restaurant public id')
class Menu(Resource):
  """ Create a menu for a restaurant """
  @owner_token_required
  @api.response(201, 'Menu successfully created')
  @api.response(404, 'Restaurant does not exists')
  @api.expect(_menu, validate=True)
  def post(self,public_id):
    """ Create a restaurant menu """
    return MenuService.create(data=request.json, public_id=public_id)

  @owner_token_required
  @api.marshal_with(_menu, envelope='Restaurant Menu')
  def get(self,public_id):
    """ Get restaurant menu """
    return MenuService.get(public_id=public_id)
