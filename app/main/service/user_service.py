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
        response_object = {
            'status':'success',
            'message':'Successfully registered'
        }
        return response_object, 201
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