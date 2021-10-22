from flask import request
from flask_restx import Resource

from app.main.service.menu_service import MenuService
from app.main.util.decorator import owner_token_required
from app.main.util.dto import MenuDto

api = MenuDto.api
_create_menu = MenuDto.add_menu
_update_menu = MenuDto.update_menu
_get_menu = MenuDto.get_menu

@api.route('/')
class MenuList(Resource):
    @owner_token_required
    @api.doc('add_menu')
    @api.response(201, 'Menu successfully added')
    @api.expect(_create_menu, validate=True)
    def post(self):
        """ 
        Add a restaurant menu 
        """
        return MenuService.add_menu(data=request.json)

@api.route('/<id>')
@api.doc(params={'id': 'An ID'})
class Menu(Resource):
    @owner_token_required
    @api.doc('get_an_existing_menu')
    @api.marshal_with(_get_menu)
    def get(self, id):
        """
        Get an existing restaurant menu
        """
        return MenuService.get_menu(id=id)

    @owner_token_required
    @api.doc('update_an_existing_menu')
    @api.response(200, 'Menu successfully updated')
    @api.response(404, 'Menu not found')
    @api.expect(_update_menu, validate=True)
    def put(self, id):
        """
        Update an existing restaurant menu
        """
        return MenuService.update_menu(id=id, data=request.json)

    @owner_token_required
    @api.doc('delete_an_existing_menu')
    @api.response(200, 'Menu successfully deleted')
    @api.response(404, 'Menu not found')
    def delete(self, id):
        """
        Delete an existing restaurant menu
        """
        return MenuService.delete_menu(id=id)
