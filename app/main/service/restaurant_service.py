from app.main import db
from app.main.model.user import User
from app.main.model.restaurant import Restaurant

def create_restaurant(data, owner_id):
    restaurant = Restaurant.query.filter_by(name=data['name']).first()
    if not restaurant:
        new_restaurant = Restaurant(
            name = data['name'],
            restaurant_type = data['restaurant_type'],
            location = data['location'],
            contact_information = data['contact_information'],
            owner_id = owner_id
        )
        create(new_restaurant)
        response_object = {
            'status':'success',
            'message':'Restaurant created successfully.'
        }
        return response_object, 201
    else:
        response_object = {
            'status':'fail',
            'message':'Restaurant already exists.'
        }
        return response_object, 409

def create(data):
    db.session.add(data)
    db.session.commit()

def get_all_restaurants():
    return Restaurant.query.all()