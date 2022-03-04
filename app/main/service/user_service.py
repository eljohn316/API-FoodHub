import datetime
from urllib import response

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
        user = User.query.filter_by(email=email).first()
        if not user:
            response_object = {
                'status' : 'fail',
                'message' : 'User not found'
            }
            return response_object, 404
        else:
            response_object = {
                'status' : 'success',
                'user' : {
                    'id' : user.id,
                    'profile_image' : user.profile_image,
                    'profile_image2' : user.profile_image2,
                    'first_name' : user.first_name,
                    'last_name' : user.last_name,
                    'email' : user.email,
                    'contact_number' : user.contact_number,
                    'user_role' : user.user_role
                }
            }
            return response_object, 200
    
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

    @staticmethod
    def set_photo(data, current_user):
        current_user = User.query.filter_by(id=current_user.get('user_id')).first()
        current_user.profile_image = data['profile_image']
        current_user.profile_image2 = data['profile_image2']
        db.session.commit()
        response_object = {
            'status' : 'success',
            'message' : 'Profile image set'
        }
        return response_object, 200

    
    @staticmethod
    def check_user_password(old_password, current_user):
        current_user = User.query.filter_by(id=current_user.get('user_id')).first_or_404(description='No user found.')
        print(current_user)
        if current_user.check_password(old_password):
            response_object = {
                'status' : 'success',
                'message' : 'Password match'
            }
            return response_object, 200
        else:
            response_object = {
                'status' : 'fail',
                'message' : 'Password does not match'
            }
            return response_object, 404

    @staticmethod
    def update_password(data, current_user):
        current_user = User.query.filter_by(id=current_user.get('user_id')).first()
        if not current_user:
            response_object = {
                'status' : 'fail',
                'message' : 'User not found'
            }
            return response_object, 404
        else:
            current_user.password = data.get('new_password')
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'Password updated'
            }
            return response_object, 200
        
    @staticmethod
    def remove_profile_image(current_user):
        user = User.query.filter_by(id=current_user.get('user_id')).first()
        if not user:
            response_object = {
                'status' : 'fail',
                'message' : 'User not found'
            }
            return response_object, 404
        else:
            user.profile_image = None
            user.profile_image2 = None
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'User profile removed'
            }
            return response_object, 200

            

