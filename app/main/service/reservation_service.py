import datetime

from app.main import db
from app.main.model import reservation
from app.main.model import restaurant
from app.main.model.user import User
from app.main.model.reservation import Reservation
from app.main.model.restaurant import Restaurant

class ReservationService:
    """
    Reservation related operations
    """

    @staticmethod
    def create_reservation(data, current_user):
        user = User.query.filter_by(id=current_user.get('user_id')).first()
        if not user:
            response_object = {
                'status' : 'fail',
                'message' : 'User does not exist'
            }
            return response_object, 404
        else:
            reservation = Reservation(
                customer_id = current_user.get('user_id'),
                restaurant_id = data['restaurant_id'],
                time = data['time'],
                date = data['date'],
                num_of_persons = data['num_of_persons'],
                customer_email = data['customer_email'],
                customer_contact_number = data['customer_contact_number'],
                is_accepted = "False",
                created_on = datetime.datetime.utcnow()
            )
            db.session.add(reservation)
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'Reservation successfully created'
            }
            return response_object, 201
        
    @staticmethod
    def update_reservation(data, reservation_id):
        reservation = Reservation.query.filter_by(id=reservation_id).first()
        if not reservation:
            response_object = {
                'status' : 'fail',
                'message' : 'Reservation does not exist'
            }
            return response_object, 404
        else:
            reservation.num_of_persons = data["num_of_persons"]
            reservation.time = data["time"]
            reservation.date = data["date"]
            reservation.customer_email = data["customer_email"]
            reservation.customer_contact_number = data["customer_contact_number"]
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'Reservation successfully updated'
            }
            return response_object, 200
    
    @staticmethod
    def cancel_reservation(reservation_id):
        reservation = Reservation.query.filter_by(id=reservation_id).first()
        if not reservation:
            response_object = {
                'status' : 'fail',
                'message' : 'Reservation does not exist'
            }
            return response_object, 404
        else:
            reservation.is_accepted = "Cancelled"
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'Reservation successfully cancelled'
            }
            return response_object, 200

    @staticmethod
    def has_already_booked(current_user, restaurant_id):
        # user = User.query.filter_by(id=current_user.get('user_id')).first()
        # print(user.reservations.all())
        # reservations = user.reservations.all()
        # for reservation in reservations:
        #     print(reservation," restaurant ids", reservation.restaurant_id)
        
        list_of_reservations = [reservation.restaurant_id for reservation in Reservation.query.filter_by(customer_id=current_user.get('user_id')).all()]
        if restaurant_id in list_of_reservations:
            response_object = {
                'status' : 'unavailable',
                'message' : 'User have already booked'
            }
            return response_object, 409
        response_object = {
            'status' : 'available',
            'message' : 'User can still book'
        }
        return response_object, 200

    @staticmethod
    def get_reservation(reservation_id):
        result = Reservation.query.filter_by(id=reservation_id).first()
        return dict(
                id = result.id,
                customer_id = result.customer_id,
                customer_email = result.customer_email,
                customer_contact_number = result.customer_contact_number,
                time = result.time,
                date = result.date,
                num_of_persons = result.num_of_persons,
                is_accepted = result.is_accepted,
                created_on = result.created_on,
                restaurant = dict(
                    restaurant_id = result.restaurant.id,
                    restaurant_image = result.restaurant.restaurant_image,
                    restaurant_thumbnail = result.restaurant.restaurant_thumbnail,
                    restaurant_thumbnail2 = result.restaurant.restaurant_thumbnail2,
                    restaurant_name = result.restaurant.restaurant_name,
                    restaurant_type = result.restaurant.restaurant_type,
                    location = result.restaurant.location,
                    date_created = result.restaurant.date_created,
                    opening_day = result.restaurant.opening_day,
                    closing_day = result.restaurant.closing_day,
                    opening_time = result.restaurant.opening_time,
                    closing_time = result.restaurant.closing_time,
                    no_of_vacancies = result.restaurant.no_of_vacancies,
                    contact_number = result.restaurant.contact_number,
                    telephone_number = result.restaurant.telephone_number
                )
            )
    
    @staticmethod
    def get_my_reservation(current_user):
        results = [
            dict(
                id = reservation.id,
                customer_id = reservation.customer_id,
                customer_email = reservation.customer_email,
                customer_contact_number = reservation.customer_contact_number,
                time = reservation.time,
                date = reservation.date,
                num_of_persons = reservation.num_of_persons,
                is_accepted = reservation.is_accepted,
                created_on = reservation.created_on,
                restaurant = dict(
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
                    telephone_number = restaurant.telephone_number
                )
            )
            for reservation, restaurant in db.session.query(Reservation, Restaurant).join(Restaurant).filter(Reservation.customer_id == current_user.get('user_id')).all()
        ]
        return results