import uuid
import datetime

from app.main import db
from app.main.model.restaurant import Restaurant

class Rest:

  @staticmethod
  def add(data, owner):
    restaurant = Restaurant.query.filter_by(restaurant_name=data['restaurant_name']).first()
    if not restaurant:
      new_restaurant = Restaurant(
        public_id = str(uuid.uuid4())[:8],
        restaurant_name = data['restaurant_name'],
        restaurant_type = data['restaurant_type'],
        business_hours = data['business_hours'],
        location = data['location'],
        contact_number = data['contact_number'],
        telephone_number = data['telephone_number'],
        date_created = datetime.datetime.utcnow(),
        owner = owner
      )
      Restaurant.add(new_restaurant)
      response_object = {
        'status':'success',
        'message':'Restaurant successfully created'
      }
      return response_object, 201
    else:
      response_object = {
        'status':'fail',
        'message':'Restaurant already exists.'
      }
      return response_object, 409

  @staticmethod
  def update(data, public_id):
    restaurant = Restaurant.query.filter_by(public_id=public_id).first()
    if not restaurant:
      response_object = {
        'status':'fail',
        'message':'Restaurant not found.'
      }
      return response_object, 404
    else:
      restaurant.restaurant_name = data['restaurant_name'],
      restaurant.restaurant_type = data['restaurant_type'],
      restaurant.business_hours = data['business_hours'],
      restaurant.location = data['location'],
      restaurant.contact_number = data['contact_number'],
      restaurant.telephone_number = data['telephone_number']
      db.session.commit()

      response_object = {
        'status':'success',
        'message':'Restaurant succesfully updated'
      }
      return response_object, 200
  
  @staticmethod
  def delete(data, public_id):
    restaurant = Restaurant.query.filter_by(public_id=public_id).first()
    if restaurant:
      Restaurant.delete(restaurant)
      response_object = {
        'status':'success',
        'message':'Successfully deleted'
      }
      return response_object, 200
    else:
      response_object = {
        'status':'fail',
        'message':'Restaurant not found.'
      }
      return response_object, 404
  
  @staticmethod
  def get_restaurants(owner):
    return Restaurant.query.filter(Restaurant.owner==owner).all()

  @staticmethod
  def get_a_restaurant(public_id):
    return Restaurant.query.filter(Restaurant.public_id==public_id).first()
  
  @staticmethod
  def get_all_restaurants():
    return Restaurant.query.all()