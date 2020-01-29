from app.main import db
from app.main.model.user import User

def create_user(data):
    user = User.query.filter_by(email=data.get('email')).first()
    if not user:
        new_user = User(
            email = data['email'],
            full_name = data['full_name'],
            contact_number = data['contact_number'],
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

def get_current_user(new_request):
    auth_token = new_request.headers.get('Authorization')
    if auth_token:
        id_resp = User.decode_auth_token(auth_token)
        user = User.query.filter_by(id=id_resp).first()
        if user:
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
        else:
            response_object = {
                'status':'fail',
                'message':'Please provide a valid token.'
            }
            return response_object, 401
    else:
        response_object = {
            "status": "fail",
            "message": "Provide a valid authorized token."
        }
        return response_object, 401