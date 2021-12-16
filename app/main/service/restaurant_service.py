import datetime

from app.main import db
from app.main.model.restaurant import Restaurant
from app.main.model.user import User
from app.main.model.menu import Menu

class RestaurantService:

    @staticmethod
    def create_restaurant(data):
        restaurant = Restaurant.query.filter_by(restaurant_name=data['restaurant_name']).first()
        if not restaurant:
            new_restaurant = Restaurant(
                # restaurant_image = data['restaurant_image'],
                # restaurant_thumbnail = data['restaurant_thumbnail'],
                # restaurant_thumbnail2 = data['restaurant_thumbnail2'],
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
    def explore_restaurants():
        results = [
            dict(
                restaurant_id = restaurant.id,
                restaurant_image = restaurant.restaurant_image,
                restaurant_thumbnail = restaurant.restaurant_thumbnail,
                restaurant_thumbnail2 = restaurant.restaurant_thumbnail2,
                restaurant_name = restaurant.restaurant_name,
                restaurant_type = restaurant.restaurant_type,
                location = restaurant.location,
                date_created = restaurant.date_created,
                opening_day = restaurant.opening_day,
                closing_day = restaurant.closing_day,
                opening_time = restaurant.opening_time,
                closing_time = restaurant.closing_time,
                no_of_vacancies = restaurant.no_of_vacancies,
                contact_number = restaurant.contact_number,
                telephone_number = restaurant.telephone_number,
                restaurant_menu = [dict(
                    menu_id = data.id,
                    menu_image = data.menu_image,
                    menu_name = data.menu_name,
                    is_available = data.is_available,
                    price = data.price
                ) for data in restaurant.restaurant_menu.all()],
                owner_id = user.id
            ) for restaurant, user in db.session.query(Restaurant, User).join(User).order_by(Restaurant.date_created.desc()).all()
        ]
        return results

    @staticmethod
    def get_owned_restaurants(current_user):
        # result = Restaurant.query.filter_by(owner_id=current_user.get('user_id')).order_by(Restaurant.date_created.desc()).all()
        # return result
        results = [
            dict(
                restaurant_id = restaurant.id,
                restaurant_image = restaurant.restaurant_image,
                restaurant_thumbnail = restaurant.restaurant_thumbnail,
                restaurant_thumbnail2 = restaurant.restaurant_thumbnail2,
                restaurant_name = restaurant.restaurant_name,
                restaurant_type = restaurant.restaurant_type,
                location = restaurant.location,
                date_created = restaurant.date_created,
                opening_day = restaurant.opening_day,
                closing_day = restaurant.closing_day,
                opening_time = restaurant.opening_time,
                closing_time = restaurant.closing_time,
                no_of_vacancies = restaurant.no_of_vacancies,
                contact_number = restaurant.contact_number,
                telephone_number = restaurant.telephone_number,
                restaurant_menu = [dict(
                    menu_id = data.id,
                    menu_image = data.menu_image,
                    menu_name = data.menu_name,
                    is_available = data.is_available,
                    price = data.price
                ) for data in restaurant.restaurant_menu.all()],
                owner_id = user.id
            ) for restaurant, user in db.session.query(Restaurant, User).join(User).filter(Restaurant.owner_id == current_user.get('user_id')).all()
        ]
        return results
     
    @staticmethod
    def get_restaurant(restaurant_id):
        # restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404('Restaurant does not exists found.')
        res, usr = db.session.query(Restaurant, User).join(User).filter(Restaurant.id == restaurant_id).first()
        result = dict(
            restaurant_id = res.id,
            restaurant_image = res.restaurant_image,
            restaurant_thumbnail = res.restaurant_thumbnail,
            restaurant_thumbnail2 = res.restaurant_thumbnail2,
            restaurant_name = res.restaurant_name,
            restaurant_type = res.restaurant_type,
            location = res.location,
            date_created = res.date_created,
            opening_day = res.opening_day,
            closing_day = res.closing_day,
            opening_time = res.opening_time,
            closing_time = res.closing_time,
            no_of_vacancies = res.no_of_vacancies,
            contact_number = res.contact_number,
            telephone_number = res.telephone_number,
            restaurant_menu = [dict(
                menu_id = data.id,
                menu_image = data.menu_image,
                menu_name = data.menu_name,
                is_available = data.is_available,
                price = data.price
            ) for data in res.restaurant_menu.all()],
            owner_details=dict(
                owner_id = usr.id,
                profile_image = usr.profile_image,
                profile_image2 = usr.profile_image2,
                email = usr.email,
                first_name = usr.first_name,
                last_name = usr.last_name,
                owner_contact_number = usr.contact_number,
                date_joined = usr.date_joined
            )
        )
        return result
    
    @staticmethod
    def get_restaurant_with_menu(restaurant_id):
        res = db.session.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
        result = dict(
            restaurant_id = res.id,
            restaurant_image = res.restaurant_image,
            restaurant_thumbnail = res.restaurant_thumbnail,
            restaurant_thumbnail2 = res.restaurant_thumbnail2,
            restaurant_name = res.restaurant_name,
            restaurant_type = res.restaurant_type,
            location = res.location,
            date_created = res.date_created,
            opening_day = res.opening_day,
            closing_day = res.closing_day,
            opening_time = res.opening_time,
            closing_time = res.closing_time,
            no_of_vacancies = res.no_of_vacancies,
            contact_number = res.contact_number,
            telephone_number = res.telephone_number,
            restaurant_menu = [dict(
                menu_id = data.id,
                menu_image = data.menu_image,
                menu_name = data.menu_name,
                is_available = data.is_available,
                price = data.price
            ) for data in res.restaurant_menu.all()]
        )
        return result
    
    @staticmethod
    def set_restaurant_image(data, restaurant_name):
        restaurant = Restaurant.query.filter_by(restaurant_name=restaurant_name).first()
        print(restaurant)
        if not restaurant:
            response_object = {
                'status':'fail',
                'message': 'Restaurant not found'
            }
            return response_object, 404
        else:
            restaurant.restaurant_image = data['restaurant_image']
            restaurant.restaurant_thumbnail = data['restaurant_thumbnail']
            restaurant.restaurant_thumbnail2 = data['restaurant_thumbnail2']
            
            db.session.commit()

            response_object = {
                'status':'success',
                'message':'Restaurant image set'
            }
            return response_object, 200