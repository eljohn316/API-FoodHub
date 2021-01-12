import uuid
import datetime

from app.main import db
from app.main.model.restaurant import Restaurant
from app.main.model.user import User

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
  def update(data, id):
    restaurant = Restaurant.query.filter_by(id=id).first()
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
  def delete(data, id):
    restaurant = Restaurant.query.filter_by(id=id).first()
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
    restaurants = [
      dict(
        restaurant_id = restaurant_info[0],
        public_id = restaurant_info[1],
        restaurant_image = restaurant_info[2],
        restaurant_name = restaurant_info[3],
        restaurant_type = restaurant_info[4],
        business_hours = restaurant_info[5],
        location = restaurant_info[6],
        contact_number = restaurant_info[7],
        telephone_number = restaurant_info[8],
        date_created = restaurant_info[9],
        owner_id = restaurant_info[10],
        profile_image = restaurant_info[11],
        full_name = restaurant_info[12],
        email = restaurant_info[13],
        password_hash = restaurant_info[14],
        owner_contact_number = restaurant_info[15],
        registered_on = restaurant_info[16],
        user_type = restaurant_info[17]
      ) for restaurant_info in db.session.query(
          Restaurant.id,
          Restaurant.public_id,
          Restaurant.restaurant_image,
          Restaurant.restaurant_name,
          Restaurant.restaurant_type,
          Restaurant.business_hours,
          Restaurant.location,
          Restaurant.contact_number,
          Restaurant.telephone_number,
          Restaurant.date_created,
          User.id,
          User.profile_image,
          User.full_name,
          User.email,
          User.password_hash,
          User.contact_number,
          User.registered_on,
          User.user_type
      ).filter_by(
        owner=owner
      ).join(
        User
      ).all()
    ]
    return restaurants

  @staticmethod
  def get_a_restaurant(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404('Restaurant not found.')
    restaurant_info = db.session.query(
      Restaurant.id,
      Restaurant.public_id,
      Restaurant.restaurant_image,
      Restaurant.restaurant_name,
      Restaurant.restaurant_type,
      Restaurant.business_hours,
      Restaurant.location,
      Restaurant.contact_number,
      Restaurant.telephone_number,
      Restaurant.date_created,
      User.id,
      User.profile_image,
      User.full_name,
      User.email,
      User.password_hash,
      User.contact_number,
      User.registered_on,
      User.user_type
    ).filter(Restaurant.id == restaurant_id).join(User).first()
    
    return dict(
      restaurant_id = restaurant_info[0],
      public_id = restaurant_info[1],
      restaurant_image = restaurant_info[2],
      restaurant_name = restaurant_info[3],
      restaurant_type = restaurant_info[4],
      business_hours = restaurant_info[5],
      location = restaurant_info[6],
      contact_number = restaurant_info[7],
      telephone_number = restaurant_info[8],
      date_created = restaurant_info[9],
      owner_id = restaurant_info[10],
      profile_image = restaurant_info[11],
      full_name = restaurant_info[12],
      email = restaurant_info[13],
      password_hash = restaurant_info[14],
      owner_contact_number = restaurant_info[15],
      registered_on = restaurant_info[16],
      user_type = restaurant_info[17]
    )
      
  @staticmethod
  def get_all_restaurants():
    restaurants = [
      dict(
        restaurant_id = restaurant_info[0],
        public_id = restaurant_info[1],
        restaurant_image = restaurant_info[2],
        restaurant_name = restaurant_info[3],
        restaurant_type = restaurant_info[4],
        business_hours = restaurant_info[5],
        location = restaurant_info[6],
        contact_number = restaurant_info[7],
        telephone_number = restaurant_info[8],
        date_created = restaurant_info[9],
        owner_id = restaurant_info[10],
        profile_image = restaurant_info[11],
        full_name = restaurant_info[12],
        email = restaurant_info[13],
        password_hash = restaurant_info[14],
        owner_contact_number = restaurant_info[15],
        registered_on = restaurant_info[16],
        user_type = restaurant_info[17]
      ) for restaurant_info in db.session.query(
          Restaurant.id,
          Restaurant.public_id,
          Restaurant.restaurant_image,
          Restaurant.restaurant_name,
          Restaurant.restaurant_type,
          Restaurant.business_hours,
          Restaurant.location,
          Restaurant.contact_number,
          Restaurant.telephone_number,
          Restaurant.date_created,
          User.id,
          User.profile_image,
          User.full_name,
          User.email,
          User.password_hash,
          User.contact_number,
          User.registered_on,
          User.user_type
      ).filter(
        Restaurant.owner_id == User.id
      ).all()
    ]
    return restaurants