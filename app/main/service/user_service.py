from app.main import db
from app.main.model.user import User

def create_user(data):
    user = User.query.filter_by(email=data.get('email')).first()
    if not user:
        new_user = User(
            email = data['email'],
            full_name = data['full_name'],
            contact_number = data['contact_number'],
            gender = data['gender'],
            username = data['username'],
            password = data['password'],
            user_type = data['user_type']
        )
        add_user(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def update_user(data, user_id):
    current_user = User.query.filter_by(id=user_id).first()
    if not current_user:
        response_object = {
            'status':'fail',
            'message':'User not found'
        }
        return response_object, 404
    else:
        current_user.email = data['email'],
        current_user.full_name = data['full_name'],
        current_user.contact_number = data['contact_number'],
        current_user.gender = data['gender'],
        current_user.username = data['username'],
        current_user.password = data['password']
        db.session.commit()

        response_object = {
            'status':'success',
            'message':'User successfully updated'
        }
        return response_object, 200
        

def get_all_users():
    return User.query.all()

def add_user(data):
    db.session.add(data)
    db.session.commit()

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

def get_current_user(data):
    return User.query.filter_by(id=data).first()