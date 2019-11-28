from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import create_user, get_all_users

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_all_users')
    @api.marshal_list_with(_user,envelope='Users')
    def get(self):
        """ List of all registered users """
        return get_all_users()
    
    @api.response(201,'User succesfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """ Creates a new User | Owner """
        data = request.json
        return create_user(data=data)
    