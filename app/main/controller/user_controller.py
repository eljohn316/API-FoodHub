from flask import request
from flask_restx import Resource

from app.main.util.dto import UserDto
from app.main.util.decorator import owner_token_required, customer_token_required
from app.main.service.user_service import UserService as user
from app.main.service.auth_helper import Auth as auth

api = UserDto.api

_out_user = UserDto.user
_in_user = UserDto.user_create
_update_user = UserDto.user_update
_image_upload = UserDto.set_profile
_update_password = UserDto.update_password

@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(_out_user, envelope='users')
    def get(self):
        """ List all registered users """
        return user.get_all_users()
    
    @api.response('User successfully created', 201)
    @api.doc('create_user')
    @api.expect(_in_user, validate=True)
    def post(self):
        """ Creates a new user """
        data = request.json
        return user.create_user(data=data)

@api.route('/<int:id>')
class User(Resource):
    @api.doc('get_a_user')
    @api.marshal_list_with(_out_user, envelope='user')
    def get(self, id):
        """ Get user by ID """
        existing_user = user.get_a_user(user_id=id)
        if not existing_user:
            api.abort(404, 'User not found')
        return existing_user
    
    @api.doc('update_user')
    @api.response('User updated successfully', 200)
    @api.expect(_update_user, validate=True)
    def put(self, id):
        """ Update user by ID """
        data = request.json
        return user.update_user(data=data, user_id=id)
    
    @api.doc('delete_a_user')
    @api.response('User successfully deleted', 200)
    @api.response('User not found', 404)
    def delete(self, id):
        """ Delete user by ID """
        return user.delete_user(user_id=id)


@api.route('/<email>')
@api.response(404, 'User not found')
class GetUserByEmail(Resource):
    @api.doc('get_user_by_email')
    def get(self, email):
        """ Get user by email"""
        # existing_user = user.get_user_by_email(email=email)
        # if not existing_user:
        #     api.abort(404, 'User not found')
        return user.get_user_by_email(email=email)

@api.route('/set-image')
class SetProfile(Resource):
    @api.doc('set_photo')
    @api.response('Profile image set', 200)
    @api.expect(_image_upload, validate=True)
    def put(self):
        """ Set profile image for user """
        current_user, status = auth.get_logged_in_user(request)
        return user.set_photo(data=request.json, current_user=current_user.get('data'))

@api.route('/check-password/<old_password>')
class CheckPassword(Resource):
    @api.doc('check_password')
    @api.response('Password match', 200)
    @api.response('Password does not match', 404)
    def get(self, old_password):
        """
        Checks the user's password
        """
        current_user, status = auth.get_logged_in_user(request)
        return user.check_user_password(old_password=old_password, current_user=current_user.get('data'))

@api.route('/update-password')
class UserPassword(Resource):
    @api.doc('update_password')
    @api.response('Password successfully updated', 200)
    @api.expect(_update_password, validate=True)
    def put(self):
        """ Update user password """
        current_user, status = auth.get_logged_in_user(request)
        return user.update_password(data=request.json, current_user=current_user.get('data'))

@api.route('/remove-image')
class UserRemoveImage(Resource):
    @api.doc('remove_profile_image')
    @api.response('User profile removed', 200)
    @api.response('User not found', 404)
    def put(self):
        current_user, status = auth.get_logged_in_user(request)
        return user.remove_profile_image(current_user=current_user.get('data'))