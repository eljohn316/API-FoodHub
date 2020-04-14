from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..util.custom_dto import UserDtoPublic
from ..service.auth_helper import Auth
from ..service.user_service import create_user, update_user, get_all_users, get_current_user
from ..util.decorator import token_required, customer_required, owner_required, selective_marshal_with

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('get_all_users')
    @selective_marshal_with(UserDtoPublic, name='Users')
    def get(self):
        """ Get all registered users """
        return get_all_users()

    @api.doc('update_user')
    @token_required
    def put(self):
        """ Update user details """
        data = request.json
        user = Auth.get_logged_in_user(request)
        current_user = user[0]["data"]["user_id"]
        return update_user(data=data, user_id=current_user)


@api.route('/current')
class CurrentUser(Resource):
    @api.doc('get_current_user')
    @token_required
    @api.marshal_list_with(_user, envelope="Current User")
    def get(self):
        """ Get the current user """
        user = Auth.get_logged_in_user(request)
        current_user = user[0]["data"]["user_id"]
        return get_current_user(current_user)

@api.route('/register')
class AddUser(Resource):
    @api.response(201,'User succesfully created.')
    @api.doc('create_user')
    @api.expect(_user, validate=True)
    def post(self):
        """ User registration """
        data = request.json
        return create_user(data=data)
