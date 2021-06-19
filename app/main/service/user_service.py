import datetime

from app.main import db
from app.main.model.user import User


class UserService:

    @staticmethod
    def create_user(data):
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            new_user = User(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = data['password'],
                contact_number = data['contact_number'],
                user_role = str(data['user_role']).capitalize(),
                date_joined = datetime.datetime.utcnow()
            )
            new_user.add(new_user)
            return UserService.generate_token(new_user)
        else:
            response_object = {
                'status' : 'fail',
                'message' : 'User already exists'
            }
            return response_object, 409
    
    @staticmethod
    def update_user(data, user_id):
        current_user = User.query.filter_by(id=user_id).first()
        if not current_user:
            response_object = {
                'status' : 'fail',
                'message' : 'User not found'
            }
            return response_object, 404
        else:
            current_user.first_name = data['first_name']
            current_user.last_name = data['last_name']
            current_user.email = data['email']
            current_user.contact_number = data['contact_number']

            db.session.commit()

            response_object = {
                'status' : 'success',
                'message' : 'User updated successfully'
            }
            return response_object, 200
    
    @staticmethod
    def delete_user(user_id):
        current_user = User.query.filter_by(id=user_id).first()
        if not current_user:
            response_object = {
                'status' : 'fail',
                'message' : 'User not found'
            }
            return response_object, 404
        else:
            db.session.delete(current_user)
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'User successfully deleted'
            }
            return response_object, 200

    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def get_a_user(user_id):
        return User.query.filter_by(id=user_id).first()
    
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def generate_token(user):
        try:
            # generate the auth token
            auth_token = user.encode_auth_token(user.id)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
                'Authorization': auth_token.decode()
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 401