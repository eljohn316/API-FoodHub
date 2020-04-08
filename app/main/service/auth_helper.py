from app.main import db
from app.main.model.user import User
from ..service.blacklist_service import save_token
from sqlalchemy import or_

class Auth:
    
    @staticmethod
    def login_user(data):
        try:
            
            user = db.session.query(User).filter(or_(User.email==data.get('username_or_email'), User.username==data.get('username_or_email'))).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500
    
    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status':'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'username': user.username,
                        'user_type': user.user_type
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status':'fail',
                'message':'Please provide a valid token.'
            }
            return response_object, 401
