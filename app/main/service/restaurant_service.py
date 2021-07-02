import datetime

from app.main import db
from app.main.model.restaurant import Restaurant
from app.main.model.user import User

class RestaurantService:

    @staticmethod
    def create_restaurant(data):
        restaurant = Restaurant.query.filter_by(restaurant_name=data['restaurant_name']).first()
        if not restaurant:
            new_restaurant = Restaurant(
                restaurant_image = data['restaurant_image'],
                restaurant_thumbnail = data['restaurant_thumbnail'],
                restaurant_name = data['restaurant_name'],
                restaurant_type = data['restaurant_type'],
                location = data['location'],
                date_created = datetime.datetime.utcnow(),
                opening_day = data['opening_day'],
                closing_day = data['closing_day'],
                opening_time = data['opening_time'],
                closing_time = data['closing_time'],
                no_of_vacancies = data['no_of_vacancies'],
                contact_number = data['contact_number'],
                telephone_number = data['telephone_number'],
                owner_id = data['owner_id']
            )
            new_restaurant.add()
            response_object = {
                'status' : 'success',
                'message' : 'Restaurant successfully added'
            }
            return response_object, 201
        else:
            response_object = {
                'status' : 'fail',
                'message' : 'Restaurant already exists'
            }
            return response_object, 409
    
    @staticmethod
    def update_restaurant(data, restaurant_id):
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
        if not restaurant:
            response_object = {
                'status' : 'fail',
                'message' : 'Restaurant not found'
            }
            return response_object, 404
        else:
            restaurant.restaurant_name = data['restaurant_name']
            restaurant.restaurant_type = data['restaurant_type']
            restaurant.location = data['location']
            restaurant.opening_day = data['opening_day']
            restaurant.closing_day = data['closing_day']
            restaurant.opening_time = data['opening_time']
            restaurant.closing_time = data['closing_time']
            restaurant.no_of_vacancies = data['no_of_vacancies']
            restaurant.contact_number = data['contact_number']
            restaurant.telephone_number = data['telephone_number']
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'Restaurant successfully updated'
            }
            return response_object, 200
    
    @staticmethod
    def delete_restaurant(restaurant_id):
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
        if not restaurant:
            response_object = {
                'status' : 'fail',
                'message' : 'Restaurant not found'
            }
            return response_object, 404
        else:
            db.session.delete(restaurant)
            db.session.commit()

            response_object = {
                'status' : 'success',
                'message' : 'Restaurant successfully deleted'
            }
            return response_object, 200
    
    @staticmethod
    def get_all_restaurants():
        return Restaurant.query.order_by(Restaurant.date_created.desc()).all()

    @staticmethod
    def get_restaurants():
        restaurants = [
        dict(
            restaurant_id = restaurant_info[0],
            restaurant_image = restaurant_info[1],
            restaurant_thumbnail = restaurant_info[2], 
            restaurant_name = restaurant_info[3],
            restaurant_type = restaurant_info[4],
            location = restaurant_info[5],
            date_created = restaurant_info[6],
            opening_day = restaurant_info[7],
            closing_day = restaurant_info[8],
            opening_time = restaurant_info[9],
            closing_time = restaurant_info[10],
            no_of_vacancies = restaurant_info[11],
            contact_number = restaurant_info[12],
            telephone_number = restaurant_info[13],
            owner_id = restaurant_info[14],
            profile_image = restaurant_info[15],
            first_name = restaurant_info[16],
            last_name = restaurant_info[17],
            email = restaurant_info[18],
            owner_contact_number = restaurant_info[19]
        ) for restaurant_info in db.session.query(
            Restaurant.id,
            Restaurant.restaurant_image,
            Restaurant.restaurant_thumbnail,
            Restaurant.restaurant_name,
            Restaurant.restaurant_type,
            Restaurant.location,
            Restaurant.date_created,
            Restaurant.opening_day,
            Restaurant.closing_day,
            Restaurant.opening_time,
            Restaurant.closing_time,
            Restaurant.no_of_vacancies,
            Restaurant.contact_number,
            Restaurant.telephone_number,
            User.id,
            User.profile_image,
            User.first_name,
            User.last_name,
            User.email,
            User.contact_number
        ).filter(
            Restaurant.owner_id == User.id
        ).all()]
        return restaurants
    
    @staticmethod
    def get_restaurant(restaurant_id):
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404('Restaurant not found.')
        restaurant_info = db.session.query(
            Restaurant.id,
            Restaurant.restaurant_image,
            Restaurant.restaurant_thumbnail,
            Restaurant.restaurant_name,
            Restaurant.restaurant_type,
            Restaurant.location,
            Restaurant.date_created,
            Restaurant.opening_day,
            Restaurant.closing_day,
            Restaurant.opening_time,
            Restaurant.closing_time,
            Restaurant.no_of_vacancies,
            Restaurant.contact_number,
            Restaurant.telephone_number,
            User.id,
            User.profile_image,
            User.first_name,
            User.last_name,
            User.email,
            User.contact_number
        ).filter(Restaurant.id == restaurant_id).join(User).first()
        return dict(
            restaurant_id = restaurant_info[0],
            restaurant_image = restaurant_info[1],
            restaurant_thumbnail = restaurant_info[2], 
            restaurant_name = restaurant_info[3],
            restaurant_type = restaurant_info[4],
            location = restaurant_info[5],
            date_created = restaurant_info[6],
            opening_day = restaurant_info[7],
            closing_day = restaurant_info[8],
            opening_time = restaurant_info[9],
            closing_time = restaurant_info[10],
            no_of_vacancies = restaurant_info[11],
            contact_number = restaurant_info[12],
            telephone_number = restaurant_info[13],
            owner_id = restaurant_info[14],
            profile_image = restaurant_info[15],
            first_name = restaurant_info[16],
            last_name = restaurant_info[17],
            email = restaurant_info[18],
            owner_contact_number = restaurant_info[19]
        )
    