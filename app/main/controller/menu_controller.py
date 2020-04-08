from flask import request, abort
from flask_restplus import Resource

from app.main.util.decorator import owner_required
from app.main.service.menu_service import create_menu, update_menu, delete_menu, get_all_menus

from ..util.dto import MenuDto

api = MenuDto.api
_menu = MenuDto.menu

@api.route('/')
class Menu(Resource):
    @api.doc('Create a menu')
    @owner_required
    @api.response(201, 'Menu created succesfully')
    @api.expect(_menu, validate=True)
    def post(self):
        """ Adds menu to a restaurant """
        data = request.json
        return create_menu(data)

    @api.doc('Get all menu')
    @owner_required
    @api.marshal_with(_menu, envelope='Menu')
    def get(self):
        """ Get all menu """
        return get_all_menus()

@api.route('/<int:menu_id>')
class MenuOperations(Resource):
    @api.doc('Update an existing menu')
    @owner_required
    @api.response(200, 'Menu successfully updated')
    def put(self, menu_id):
        """ Update menu """
        data = request.json
        return update_menu(data=data,menu_id=menu_id)

    @api.doc('Delete an existing menu')
    @owner_required
    @api.response(200, 'Menu successfully deleted')
    def delete(self,menu_id):
        """ Delete menu """
        return delete_menu(menu_id=menu_id)