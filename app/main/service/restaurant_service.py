import uuid

from app.main import db
from app.main.model.user import User
from app.main.model.restaurant import Restaurant

def create_restaurant(data, owner_id):
    restaurant = Restaurant.query.filter_by(name=data['name']).first()
    if not restaurant:
        new_restaurant = Restaurant(
            public_id = str(uuid.uuid4()),
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

def update_restaurant(data, public_id):
    restaurant = Restaurant.query.filter_by(public_id=public_id).first()
    if restaurant is None:
        response_object = {
            'status':'fail',
            'message':'No restaurant found.'
        }
        return response_object, 404
    else:
        restaurant.name = data['name'],
        restaurant.restaurant_type = data['restaurant_type'],
        restaurant.location = data['location'],
        restaurant.contact_information = data['contact_information']
        db.session.commit()
        response_object = {
            'status':'success',
            'message':'Restaurant succesfully updated.'
        }
        return response_object, 200

def delete_restaurant(restaurant_id, owner_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
    if restaurant.owner_id == owner_id:
        db.session.delete(restaurant)
        db.session.commit()
        
        response_object = {
            'status':'success',
            'message':'Restaurant successfully deleted.'
        }
        return response_object, 200
    else:
        response_object = {
            'status':'fail',
            'message':'No restaurant found.'
        }
        return response_object, 404

def create(data):
    db.session.add(data)
    db.session.commit()

def get_all_restaurants():
    return Restaurant.query.all()

def get_restaurants_owned(owner_id):
    return Restaurant.query.filter_by(owner_id=owner_id).all()

def get_a_restaurant(public_id):
    return Restaurant.query.filter_by(public_id=public_id).first()