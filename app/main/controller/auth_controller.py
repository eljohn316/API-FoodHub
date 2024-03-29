from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth as auth
from app.main.util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user_login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout_a_user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return auth.logout_user(data=auth_header)

@api.route('/current-user')
class CurrentUser(Resource):
    """
    Get Logged In User
    """
    @api.doc('get_current_user')
    def post(self):
        return auth.get_logged_in_user(request)